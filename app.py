import streamlit as st
import json
from schemas import VeoPromptSchema, UnstructuredInput
from gemini_service import GeminiSchemaEnforcer

# Page configuration
st.set_page_config(
    page_title="Veo Schema Enforcer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'gemini_enforcer' not in st.session_state:
    st.session_state.gemini_enforcer = GeminiSchemaEnforcer()
if 'structured_output' not in st.session_state:
    st.session_state.structured_output = None
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""

# Header
st.markdown('<h1 class="main-header">🎬 Veo Schema-Enforcing API</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Transform unstructured text into validated Veo video generation prompts</p>', unsafe_allow_html=True)

# Sidebar with information and examples
with st.sidebar:
    st.header("📖 About")
    st.info(
        "This application uses **Gemini 1.5 Flash** with function calling to convert "
        "natural language video descriptions into structured JSON prompts optimized for "
        "**Google Veo** video generation."
    )
    
    st.header("✨ Example Prompts")
    
    examples = {
        "🎥 Cinematic Scene": "A detective walks through rainy noir streets at night, neon lights reflecting in puddles, shot like a classic film noir with dramatic shadows",
        
        "📱 Product Video": "Show a sleek black smartphone slowly rotating on a white minimalist background with dramatic studio lighting highlighting its edges",
        
        "🌅 Nature Documentary": "Aerial drone footage of a lion pride walking across African savanna during golden hour sunset, documentary style with natural sounds",
        
        "🏃 Action Shot": "A parkour athlete jumps between urban rooftops at sunset, captured with dynamic camera following the motion, energetic and thrilling",
        
        "🍳 Cooking Tutorial": "Close-up of hands chopping fresh vegetables on a wooden cutting board, bright kitchen lighting, warm and inviting atmosphere"
    }
    
    for name, prompt in examples.items():
        if st.button(name, use_container_width=True):
            st.session_state.input_text = prompt
            st.rerun()

# Main content area
tab1, tab2, tab3 = st.tabs(["🎯 Generate Prompt", "📋 View Schema", "ℹ️ How It Works"])

with tab1:
    st.header("Input Your Video Description")
    
    # Input text area
    user_input = st.text_area(
        "Describe your desired video in natural language:",
        value=st.session_state.input_text,
        height=150,
        placeholder="Example: A woman walking through a futuristic city at night with neon lights...",
        help="Enter any natural language description of the video you want to generate"
    )
    
    col1, col2, col3 = st.columns([1, 1, 3])
    
    with col1:
        generate_button = st.button("🚀 Generate Schema", type="primary", use_container_width=True)
    
    with col2:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    if clear_button:
        st.session_state.structured_output = None
        st.session_state.input_text = ""
        st.rerun()
    
    # Generate structured output
    if generate_button and user_input:
        with st.spinner("🔄 Processing with Gemini AI..."):
            try:
                structured_output = st.session_state.gemini_enforcer.normalize_to_schema(user_input)
                st.session_state.structured_output = structured_output
                st.success("✅ Schema generated successfully!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    # Display results
    if st.session_state.structured_output:
        st.divider()
        st.header("📊 Structured Output")
        
        # Create two columns for better layout
        col_left, col_right = st.columns([1, 1])
        
        with col_left:
            st.subheader("🎭 Subject & Scene")
            
            output = st.session_state.structured_output
            
            st.markdown("**Subject:**")
            st.json({
                "description": output.subject.description,
                "action": output.subject.action,
                "wardrobe": output.subject.wardrobe,
                "expression": output.subject.expression
            })
            
            st.markdown("**Scene:**")
            st.json({
                "location": output.scene.location,
                "time_of_day": output.scene.time_of_day,
                "lighting": output.scene.lighting,
                "ambiance": output.scene.ambiance,
                "weather": output.scene.weather
            })
        
        with col_right:
            st.subheader("🎥 Technical Specs")
            
            st.markdown("**Shot Composition:**")
            st.json({
                "framing": output.shot.framing,
                "lens": output.shot.lens,
                "camera_equipment": output.shot.camera_equipment,
                "frame_rate": output.shot.frame_rate
            })
            
            st.markdown("**Camera Motion:**")
            st.json({
                "type": output.camera_motion.type,
                "description": output.camera_motion.description
            })
            
            st.markdown("**Style & Parameters:**")
            st.json({
                "style": output.style,
                "duration_seconds": output.duration_seconds,
                "aspect_ratio": output.aspect_ratio,
                "generate_audio": output.generate_audio
            })
        
        st.divider()
        
        # Complete JSON output
        st.subheader("📝 Complete JSON Output")
        st.markdown("*Copy this JSON to use with Veo API:*")
        
        json_output = output.model_dump_json(indent=2)
        st.code(json_output, language="json")
        
        # Download button
        st.download_button(
            label="⬇️ Download JSON",
            data=json_output,
            file_name="veo_prompt.json",
            mime="application/json",
            use_container_width=True
        )

with tab2:
    st.header("📋 Veo Prompt Schema Structure")
    st.markdown("""
    This is the complete schema structure that all outputs will conform to:
    """)
    
    # Display the schema using streamlit-pydantic
    st.json({
        "subject": {
            "description": "string (required)",
            "action": "string (required)",
            "wardrobe": "string (optional)",
            "expression": "string (optional)"
        },
        "scene": {
            "location": "string (required)",
            "time_of_day": "string (required)",
            "lighting": "string (required)",
            "ambiance": "string (optional)",
            "weather": "string (optional)"
        },
        "shot": {
            "framing": "string (required)",
            "lens": "string (optional)",
            "camera_equipment": "string (optional)",
            "frame_rate": "string (optional)"
        },
        "camera_motion": {
            "type": "string (required)",
            "description": "string (optional)"
        },
        "style": "string (required)",
        "audio": {
            "ambient": "string (optional)",
            "voice_tone": "string (optional)",
            "music_style": "string (optional)"
        },
        "duration_seconds": "integer [4, 6, 8]",
        "aspect_ratio": "string [16:9, 9:16]",
        "generate_audio": "boolean",
        "negative_prompt": "array of strings (optional)"
    })

with tab3:
    st.header("ℹ️ How It Works")
    
    st.markdown("""
    ### 🔄 Processing Pipeline
    
    1. **Input**: You provide an unstructured text description
    2. **AI Processing**: Gemini 1.5 Flash analyzes the text using function calling
    3. **Schema Enforcement**: Pydantic validates the output structure
    4. **Output**: Perfectly formatted JSON ready for Veo API
    
    ### 🛠️ Tech Stack
    
    - **AI Model**: Google Gemini 1.5 Flash with function calling
    - **Validation**: Pydantic BaseModel
    - **UI Framework**: Streamlit
    - **Deployment**: Streamlit Community Cloud
    
    ### 📚 Key Features
    
    - ✅ Automatic schema validation
    - ✅ Professional cinematography defaults
    - ✅ Support for all Veo parameters
    - ✅ Industry-standard technical specifications
    - ✅ One-click JSON export
    
    ### 🎯 Use Cases
    
    - Product demonstration videos
    - Cinematic storytelling
    - Documentary footage
    - Marketing content
    - Social media clips
    - Educational videos
    """)

# Footer
st.divider()
st.markdown(
    "<p style='text-align: center; color: #666;'>Built with Streamlit 🎈 | Powered by Gemini AI 🤖 | Optimized for Veo 🎬</p>",
    unsafe_allow_html=True
)

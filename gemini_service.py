import google.generativeai as genai
import streamlit as st
from schemas import VeoPromptSchema

class GeminiSchemaEnforcer:
    def __init__(self):
        """Initialize Gemini with function calling capabilities using Streamlit secrets"""
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        except Exception as e:
            st.error(f"Failed to initialize Gemini: {str(e)}")
            st.stop()
        
    def _create_function_declaration(self):
        """Create function declaration for Veo prompt structure"""
        return {
            "name": "create_veo_prompt",
            "description": "Convert unstructured video description into a structured Veo video generation prompt with all required elements: subject, scene, shot composition, camera motion, style, and technical parameters.",
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {
                        "type": "object",
                        "description": "Subject/character specifications",
                        "properties": {
                            "description": {"type": "string", "description": "Detailed description of subject"},
                            "action": {"type": "string", "description": "What the subject is doing"},
                            "wardrobe": {"type": "string", "description": "Clothing details"},
                            "expression": {"type": "string", "description": "Facial expression"}
                        },
                        "required": ["description", "action"]
                    },
                    "scene": {
                        "type": "object",
                        "description": "Scene environment specifications",
                        "properties": {
                            "location": {"type": "string"},
                            "time_of_day": {"type": "string"},
                            "lighting": {"type": "string"},
                            "ambiance": {"type": "string"},
                            "weather": {"type": "string"}
                        },
                        "required": ["location", "time_of_day", "lighting"]
                    },
                    "shot": {
                        "type": "object",
                        "properties": {
                            "framing": {"type": "string", "description": "Shot framing type"},
                            "lens": {"type": "string"},
                            "camera_equipment": {"type": "string"},
                            "frame_rate": {"type": "string"}
                        },
                        "required": ["framing"]
                    },
                    "camera_motion": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string", "description": "Camera motion type"},
                            "description": {"type": "string"}
                        },
                        "required": ["type"]
                    },
                    "style": {"type": "string", "description": "Visual style"},
                    "audio": {
                        "type": "object",
                        "properties": {
                            "ambient": {"type": "string"},
                            "voice_tone": {"type": "string"},
                            "music_style": {"type": "string"}
                        }
                    },
                    "duration_seconds": {
                        "type": "integer", 
                        "description": "Video duration in seconds (typically 4, 6, or 8)"
                    },
                    "aspect_ratio": {
                        "type": "string",
                        "description": "Video aspect ratio (typically 16:9 or 9:16)"
                    },
                    "generate_audio": {"type": "boolean"},
                    "negative_prompt": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["subject", "scene", "shot", "camera_motion", "style"]
            }
        }
    
    def normalize_to_schema(self, unstructured_text: str) -> VeoPromptSchema:
        """
        Convert unstructured text to structured Veo prompt using function calling
        """
        function_declaration = self._create_function_declaration()
        tools = [{"function_declarations": [function_declaration]}]
        
        enhanced_prompt = f"""
        Analyze the following video description and extract all relevant elements to create a complete Veo video generation prompt.
        
        Fill in missing details with professional, cinematic defaults based on the context.
        For camera specifications, use industry-standard equipment and techniques.
        For lighting and ambiance, infer from the described mood or setting.
        
        For duration_seconds, use 8 for detailed scenes, 6 for medium length, or 4 for short clips.
        For aspect_ratio, use "16:9" for landscape/cinematic or "9:16" for vertical/mobile content.
        
        Video Description:
        {unstructured_text}
        
        Extract and structure ALL elements: subject details, scene setup, camera work, style, and technical parameters.
        """
        
        try:
            response = self.model.generate_content(
                enhanced_prompt,
                tools=tools,
                tool_config={'function_calling_config': 'ANY'}
            )
            
            if response.candidates[0].content.parts[0].function_call:
                function_call = response.candidates[0].content.parts[0].function_call
                structured_data = dict(function_call.args)
                return VeoPromptSchema(**structured_data)
            else:
                raise ValueError("Gemini did not return a function call")
        except Exception as e:
            raise Exception(f"Error during schema normalization: {str(e)}")

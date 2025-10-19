Here's a complete, production-ready README.md file you can directly copy and paste:

text
# 🎬 Veo Schema-Enforcing API: Unstructured-to-JSON Normalizer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://veo-json-prompt.streamlit.app)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Pydantic v2](https://img.shields.io/badge/pydantic-v2-E92063.svg)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Transform unstructured text descriptions into validated JSON prompts for Google Veo video generation**

An intelligent API powered by Google Gemini 2.0 Flash that converts natural language video descriptions into structured, production-ready JSON prompts optimized for Google's Veo video generation model.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Project Objective](#-project-objective)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Prerequisites](#-prerequisites)
- [Step-by-Step Implementation](#-step-by-step-implementation)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [API Schema Documentation](#-api-schema-documentation)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Example Outputs](#-example-outputs)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Project Overview

The **Veo Schema-Enforcing API** is an intelligent normalizer that bridges the gap between human creativity and structured AI video generation. It accepts high-level, unstructured text descriptions and returns perfectly validated JSON objects conforming to Google Veo's video generation schema.

### The Problem

Video generation APIs like Google Veo require highly structured JSON inputs with specific fields for:
- Subject details (description, action, wardrobe, expression)
- Scene specifications (location, time of day, lighting, ambiance)
- Camera work (shot composition, motion, technical specs)
- Style and audio parameters
- Technical constraints (duration, aspect ratio)

Creating these structured prompts manually is:
- ⏱️ **Time-consuming** - Takes 5-10 minutes per prompt
- ❌ **Error-prone** - Easy to miss required fields
- 🧠 **Cognitively demanding** - Requires knowledge of cinematography

### The Solution

This API automates the entire process using:
- **Gemini 2.0 Flash** with function calling for intelligent extraction
- **Pydantic v2** for bulletproof schema validation
- **Streamlit UI** for easy interaction and deployment

**Result**: Generate production-ready video prompts in 2-5 seconds.

---

## 🎯 Project Objective

### Primary Goal

Build a robust API endpoint that accepts any piece of high-level, unstructured text and reliably returns a perfectly validated JSON object based on a predefined Veo video generation schema.

### Key Objectives

1. **Schema Enforcement** - Ensure 100% compliance with Veo's prompt structure using Pydantic validation
2. **AI-Powered Intelligence** - Use Gemini's function calling to intelligently extract and infer video elements
3. **Production-Ready** - Provide a deployable Streamlit interface for immediate use
4. **Type Safety** - Leverage Pydantic for compile-time type checking and runtime validation
5. **Extensibility** - Design for easy adaptation to other structured prompt requirements

### Success Metrics

- ✅ 100% valid JSON output conforming to schema
- ✅ Response time under 5 seconds
- ✅ Zero manual intervention required
- ✅ Handles edge cases (vague inputs, missing details)
- ✅ Production deployment on cloud platform

---

## ✨ Features

### Core Capabilities

- 🤖 **AI-Powered Schema Extraction** - Gemini 2.0 Flash with function calling
- ✅ **Pydantic Validation** - Industry-standard data validation with type safety
- 🎨 **Interactive UI** - Beautiful Streamlit interface with dark mode
- ⚡ **Fast Generation** - 2-5 second response time
- 💾 **JSON Export** - One-click download of generated prompts
- 📋 **Example Library** - Pre-built prompts for inspiration
- 🔒 **Secure** - API keys managed through encrypted secrets
- 📱 **Responsive** - Works on desktop, tablet, and mobile
- 🚀 **Cloud-Ready** - Deploy to Streamlit Community Cloud in minutes
- 🎯 **Smart Defaults** - Fills missing details with professional cinematography standards

### Advanced Features

- **Intelligent Inference** - Deduces camera equipment, lighting, and technical specs from context
- **Cinematography Standards** - Applies industry-standard defaults for professional output
- **Multi-format Export** - JSON with proper indentation and structure
- **Error Handling** - Graceful fallbacks with detailed error messages
- **Real-time Validation** - Instant feedback on generated schemas

---

## 🛠️ Tech Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **AI Model** | Google Gemini 2.0 Flash | Latest | Schema extraction via function calling |
| **Validation** | Pydantic | 2.5.0 | Type-safe data validation and serialization |
| **UI Framework** | Streamlit | 1.38.0 | Interactive web application interface |
| **Language** | Python | 3.12+ | Core implementation language |
| **API Library** | google-generativeai | 0.3.2 | Gemini API integration |
| **Deployment** | Streamlit Community Cloud | - | Serverless cloud hosting |

### Why These Technologies?

- **Gemini 2.0 Flash**: Latest model with native function calling, 2x faster than 1.5 Pro
- **Pydantic v2**: 20x faster validation than v1, excellent error messages
- **Streamlit**: Zero-config deployment, auto-reloading, built-in secrets management
- **Python 3.12+**: Latest performance improvements and type hints

---

## 🏗️ Architecture

┌──────────────────────────────────────────────────────────────┐
│ User Input (Natural Language) │
│ "A detective walks through rainy noir streets..." │
└───────────────────────────┬──────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ Streamlit Interface (app.py) │
│ - Input validation - UI rendering - Error handling │
│ - Example management - Download functionality │
└───────────────────────────┬──────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ Gemini Service (gemini_service.py) │
│ - Function declaration builder │
│ - API communication layer │
│ - Response parsing and error handling │
└───────────────────────────┬──────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ Google Gemini 2.0 Flash (Function Calling) │
│ Analyzes text → Extracts elements → Returns structured JSON │
└───────────────────────────┬──────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ Pydantic Validation (schemas.py) │
│ - VeoPromptSchema validation │
│ - Type checking - Default population - Enum validation │
└───────────────────────────┬──────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ Validated JSON Output │
│ Ready for Google Veo video generation API │
└──────────────────────────────────────────────────────────────┘

text

---

## 📦 Prerequisites

### System Requirements

- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **Python**: Version 3.12 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Internet**: Stable connection for API calls
- **Disk Space**: ~500MB for virtual environment and dependencies

### Required Accounts & API Keys

1. **Google AI Studio Account**
   - Sign up: https://makersuite.google.com/
   - Create API key: https://makersuite.google.com/app/apikey
   - Cost: Free tier includes 60 requests/minute

2. **GitHub Account** (for deployment)
   - Sign up: https://github.com/signup
   - Required for Streamlit Cloud deployment

3. **Streamlit Community Cloud Account** (for hosting)
   - Sign up: https://share.streamlit.io/
   - Free tier includes unlimited public apps

### Development Tools

- **Text Editor/IDE**: VS Code, PyCharm, Sublime Text, or any code editor
- **Terminal**: Command Prompt, PowerShell, Terminal, or Git Bash
- **Git**: Version control (download from https://git-scm.com/)

---

## 🚀 Step-by-Step Implementation

Follow these steps to implement the project on **any system** (Windows, macOS, or Linux).

### Step 1: Environment Setup

#### 1.1 Install Python

**Windows:**
Download Python 3.12+ from https://www.python.org/downloads/
During installation, check "Add Python to PATH"
Verify installation:
python --version

text

**macOS:**
Install using Homebrew
brew install python@3.12

Or download from https://www.python.org/downloads/
Verify installation:
python3 --version

text

**Linux (Ubuntu/Debian):**
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip
python3.12 --version

text

#### 1.2 Clone or Create Project Directory

**Option A: Clone from GitHub (if available)**
git clone https://github.com/YOUR_USERNAME/veo-schema-api.git
cd veo-schema-api

text

**Option B: Create from scratch**
Create project directory
mkdir veo-schema-api
cd veo-schema-api

Initialize git
git init

text

### Step 2: Create Project Files

Create the following file structure:

veo-schema-api/
├── app.py
├── schemas.py
├── gemini_service.py
├── requirements.txt
├── .gitignore
└── README.md

text

#### 2.1 Create `requirements.txt`

streamlit==1.38.0
google-generativeai==0.3.2
pydantic==2.5.0

text

#### 2.2 Create `.gitignore`

.streamlit/secrets.toml
.streamlit/
venv/
pycache/
*.pyc
.env
*.log
.DS_Store
*.egg-info/
dist/
build/

text

#### 2.3 Create Core Files

Copy the code for `app.py`, `schemas.py`, and `gemini_service.py` from the project implementation sections above.

### Step 3: Virtual Environment Setup

#### 3.1 Create Virtual Environment

**Windows:**
Create virtual environment
python -m venv venv

Activate it
venv\Scripts\activate

You should see (venv) in your prompt
text

**macOS/Linux:**
Create virtual environment
python3 -m venv venv

Activate it
source venv/bin/activate

You should see (venv) in your prompt
text

#### 3.2 Upgrade pip

Upgrade pip to latest version
pip install --upgrade pip

text

### Step 4: Install Dependencies

Install all required packages
pip install -r requirements.txt

Verify installation
pip list

text

Expected output should include:
- streamlit (1.38.0)
- google-generativeai (0.3.2)
- pydantic (2.5.0)

### Step 5: Configure API Keys

#### 5.1 Create Secrets Directory

**Windows:**
mkdir .streamlit
type nul > .streamlit\secrets.toml

text

**macOS/Linux:**
mkdir -p .streamlit
touch .streamlit/secrets.toml

text

#### 5.2 Add Your API Key

Open `.streamlit/secrets.toml` in your text editor and add:

GEMINI_API_KEY = "AIzaSyC_your_actual_api_key_here"

text

**Get Your API Key:**
1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key (starts with `AIza...`)
4. Paste it in `secrets.toml` (must use double quotes!)

**Security Note:** Never commit `secrets.toml` to GitHub!

### Step 6: Run Locally

#### 6.1 Start the Application

Make sure virtual environment is activated
streamlit run app.py

text

#### 6.2 Access the Application

The terminal will show:
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501

text

Open [**http://localhost:8501**](http://localhost:8501) in your web browser.

### Step 7: Test the Application

#### 7.1 Basic Test

1. Enter this prompt in the text area:
Create a video of a chef preparing sushi in a modern kitchen

text

2. Click **"🚀 Generate Schema"**

3. Wait 2-5 seconds for processing

4. Verify you see structured JSON output with:
- Subject details
- Scene specifications
- Camera work
- Technical parameters

#### 7.2 Test Example Prompts

Click the example buttons in the sidebar:
- 🎥 Cinematic Scene
- 📱 Product Video
- 🌅 Nature Documentary
- 🏃 Action Shot
- 🍳 Cooking Tutorial

Verify each generates valid JSON.

#### 7.3 Test Download

1. Generate a schema
2. Click **"⬇️ Download JSON"**
3. Verify the `.json` file downloads correctly

### Step 8: Version Control Setup

#### 8.1 Initial Commit

Check what will be committed
git status

Verify secrets.toml is NOT listed (should be gitignored)
Add all files
git add .

Commit
git commit -m "Initial commit: Veo Schema-Enforcing API"

text

#### 8.2 Create GitHub Repository

**Option A: Using GitHub Website**
1. Go to https://github.com/new
2. Repository name: `veo-schema-api`
3. Set to **Public** (required for free Streamlit hosting)
4. Don't initialize with README
5. Click **"Create repository"**

**Option B: Using GitHub CLI**
gh repo create veo-schema-api --public --source=. --remote=origin

text

#### 8.3 Push to GitHub

Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/veo-schema-api.git

Push code
git branch -M main
git push -u origin main

text

### Step 9: Deploy to Streamlit Cloud

#### 9.1 Sign Up for Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click **"Sign up"**
3. Choose **"Continue with GitHub"**
4. Authorize Streamlit to access your repositories

#### 9.2 Deploy Your App

1. Click **"New app"** in the upper-right corner

2. Fill in deployment details:
Repository: YOUR_USERNAME/veo-schema-api
Branch: main
Main file path: app.py

text

3. Click **"Advanced settings"**

4. **Add Secrets** in TOML format:
GEMINI_API_KEY = "AIzaSyC_your_actual_api_key_here"

text

5. Set Python version: **3.12**

6. Click **"Save"**

7. Click **"Deploy!"**

#### 9.3 Monitor Deployment

Watch the build logs as Streamlit:
1. Clones your repository
2. Installs dependencies
3. Starts your app

**Deployment time**: 2-5 minutes

### Step 10: Access Your Deployed App

Once deployment completes, your app will be available at:
https://your-app-name.streamlit.app

text

Share this URL with anyone! The app is now publicly accessible.

### Step 11: Update Your Deployment

Whenever you make changes:

Make code changes
Then commit and push
git add .
git commit -m "Update: description of changes"
git push

Streamlit Cloud auto-deploys!
text

Your app will automatically redeploy within 1-2 minutes.

---

## ⚙️ Configuration

### Environment Variables

All configuration is managed through `.streamlit/secrets.toml`:

Required: Gemini API Key
GEMINI_API_KEY = "AIzaSyC_your_api_key_here"

Optional: Custom model (default: gemini-2.0-flash-exp)
MODEL_NAME = "gemini-2.0-flash-lite"
Optional: Max tokens (default: 2048)
MAX_OUTPUT_TOKENS = 2048
text

### Model Selection

Edit `gemini_service.py` to change the AI model:

Available models (choose one):
self.model = genai.GenerativeModel('gemini-2.0-flash-exp') # Default - best balance
self.model = genai.GenerativeModel('gemini-2.0-flash-lite') # Faster, cheaper
self.model = genai.GenerativeModel('gemini-2.5-flash') # Advanced reasoning

text

### Streamlit Configuration

Create `.streamlit/config.toml` for UI customization:

[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"

[server]
maxUploadSize = 200

text

---

## 📖 Usage Guide

### Basic Usage

1. **Start Application**
streamlit run app.py

text

2. **Enter Video Description**
- Natural language description
- Any level of detail
- Can include or omit technical specs

3. **Generate Schema**
- Click "🚀 Generate Schema"
- Wait 2-5 seconds
- Review structured output

4. **Download or Copy**
- Download as JSON file
- Or copy from code block

### Input Examples

**Simple Input:**
A dog running in a park

text

**Detailed Input:**
A golden retriever running through a sunny park during golden hour,
shot with a steadicam following from the side, cinematic style

text

**Technical Input:**
Close-up product shot of a luxury watch rotating 360 degrees on black
velvet, dramatic studio lighting with rim light, shot on RED camera
with 85mm macro lens, 24fps

text

### Output Formats

**JSON Structure:**
{
"subject": {...},
"scene": {...},
"shot": {...},
"camera_motion": {...},
"style": "...",
"audio": {...},
"duration_seconds": 8,
"aspect_ratio": "16:9",
"generate_audio": true,
"negative_prompt": [...]
}

text

### Advanced Features

#### Batch Processing

Create `batch_process.py`:

from gemini_service import GeminiSchemaEnforcer
import json

enforcer = GeminiSchemaEnforcer()

prompts = [
"A sunset over mountains",
"A chef cooking pasta",
"A robot walking"
]

results = []
for prompt in prompts:
schema = enforcer.normalize_to_schema(prompt)
results.append(schema.model_dump())

with open('batch_results.json', 'w') as f:
json.dump(results, f, indent=2)

text

Run with:
python batch_process.py

text

---

## 📐 API Schema Documentation

### VeoPromptSchema Structure

class VeoPromptSchema(BaseModel):
subject: Subject # Required
scene: Scene # Required
shot: ShotComposition # Required
camera_motion: CameraMotion # Required
style: str # Required
audio: Optional[Audio] = None # Optional
duration_seconds: int = 8 # Default: 8
aspect_ratio: str = "16:9" # Default: 16:9
generate_audio: bool = True # Default: True
negative_prompt: Optional[List[str]] = None # Optional

text

### Nested Models

#### Subject
class Subject(BaseModel):
description: str # Required - detailed description
action: str # Required - what subject is doing
wardrobe: Optional[str] # Optional - clothing/appearance
expression: Optional[str] # Optional - facial expression

text

#### Scene
class Scene(BaseModel):
location: str # Required - physical location
time_of_day: str # Required - time (golden hour, night, etc.)
lighting: str # Required - lighting conditions
ambiance: Optional[str] # Optional - mood/atmosphere
weather: Optional[str] # Optional - weather conditions

text

#### ShotComposition
class ShotComposition(BaseModel):
framing: str # Required - shot type
lens: Optional[str] # Optional - lens specification
camera_equipment: Optional[str] # Optional - camera equipment
frame_rate: str = "24fps" # Default: 24fps

text

#### CameraMotion
class CameraMotion(BaseModel):
type: str # Required - motion type
description: Optional[str] # Optional - detailed movement

text

#### Audio
class Audio(BaseModel):
ambient: Optional[str] # Optional - environmental sounds
voice_tone: Optional[str] # Optional - voice characteristics
music_style: Optional[str] # Optional - background music

text

### Field Constraints

| Field | Type | Validation | Example Values |
|-------|------|-----------|----------------|
| duration_seconds | int | 4, 6, or 8 | `8` |
| aspect_ratio | str | "16:9" or "9:16" | `"16:9"` |
| framing | str | Any shot type | `"wide shot"`, `"close-up"` |
| camera_motion.type | str | Any motion type | `"dolly"`, `"crane"`, `"static"` |

---

## 🌐 Deployment

### Streamlit Community Cloud (Recommended)

**Pros:**
- ✅ Free for public apps
- ✅ One-click deployment
- ✅ Auto-redeploy on git push
- ✅ Built-in secrets management
- ✅ HTTPS by default

**Deployment Steps:**

1. Push code to GitHub (public repo)
2. Go to https://share.streamlit.io/
3. Click "New app"
4. Select repository and branch
5. Add secrets
6. Deploy

**Cost:** Free

### Alternative Platforms

#### Heroku

Create Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

Deploy
heroku create veo-schema-api
git push heroku main

text

**Cost:** $7/month (Eco Dynos)

#### AWS EC2

SSH into instance
ssh -i key.pem ubuntu@your-ip

Setup
sudo apt update
git clone your-repo
cd your-repo
pip install -r requirements.txt

Run with screen
screen -S streamlit
streamlit run app.py --server.port 8501

text

**Cost:** ~$10/month (t2.micro)

#### Google Cloud Run

Create Dockerfile
docker build -t veo-api .
gcloud run deploy --image gcr.io/PROJECT/veo-api

text

**Cost:** Pay per use (~$5-20/month)

### Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Repository is public
- [ ] `.gitignore` excludes secrets
- [ ] `requirements.txt` is up to date
- [ ] App works locally
- [ ] API key is ready
- [ ] Secrets configured in cloud platform
- [ ] Domain/URL chosen
- [ ] App tested after deployment

---

## 📁 Project Structure

veo-schema-api/
│
├── app.py # Main Streamlit application
│ ├── UI components and layout
│ ├── Input handling and validation
│ ├── Example prompts sidebar
│ ├── Output rendering (tabs)
│ └── Download functionality
│
├── schemas.py # Pydantic data models
│ ├── VeoPromptSchema (main)
│ ├── Subject model
│ ├── Scene model
│ ├── ShotComposition model
│ ├── CameraMotion model
│ ├── Audio model
│ ├── Enums (AspectRatio, Duration)
│ └── Validation logic
│
├── gemini_service.py # Gemini AI integration
│ ├── GeminiSchemaEnforcer class
│ ├── Function declaration builder
│ ├── API communication layer
│ ├── Response parsing
│ └── Error handling
│
├── requirements.txt # Python dependencies
│ ├── streamlit==1.38.0
│ ├── google-generativeai==0.3.2
│ └── pydantic==2.5.0
│
├── .streamlit/ # Streamlit configuration
│ └── secrets.toml # API keys (not in repo)
│
├── .gitignore # Git exclusions
├── README.md # This documentation
└── LICENSE # MIT License

text

### File Descriptions

**`app.py`** (Main Application)
- Streamlit UI implementation
- User input handling
- Example prompt management
- Output formatting and display
- JSON export functionality
- Error handling and user feedback

**`schemas.py`** (Data Models)
- Pydantic v2 model definitions
- Type hints and validation rules
- Default value specifications
- JSON schema generation
- Custom validators

**`gemini_service.py`** (AI Integration)
- Gemini API configuration
- Function calling implementation
- Prompt engineering
- Response parsing
- Error handling and retries

**`requirements.txt`** (Dependencies)
- Production dependencies only
- Pinned versions for stability
- Compatible with Python 3.12+

---

## 💡 Example Outputs

### Example 1: Product Video

**Input:**
Show a sleek smartphone rotating on white background with dramatic lighting

text

**Output:**
{
"subject": {
"description": "Modern black smartphone with glass and metal finish",
"action": "rotating 360 degrees on minimalist pedestal",
"wardrobe": null,
"expression": null
},
"scene": {
"location": "minimalist white studio",
"time_of_day": "studio lighting",
"lighting": "dramatic studio lighting with key light and rim light",
"ambiance": "clean and professional",
"weather": null
},
"shot": {
"framing": "medium close-up product shot",
"lens": "85mm macro",
"camera_equipment": "RED Komodo",
"frame_rate": "24fps"
},
"camera_motion": {
"type": "static",
"description": "camera remains fixed while product rotates on turntable"
},
"style": "commercial product photography with high contrast",
"audio": null,
"duration_seconds": 8,
"aspect_ratio": "16:9",
"generate_audio": false,
"negative_prompt": ["text overlays", "distracting elements"]
}

text

### Example 2: Cinematic Scene

**Input:**
A detective walks through rainy noir streets at night, neon lights reflecting in puddles

text

**Output:**
{
"subject": {
"description": "Middle-aged detective in classic trench coat and fedora",
"action": "walking slowly through rain-soaked street",
"wardrobe": "dark trench coat, fedora hat, business suit",
"expression": "serious and contemplative"
},
"scene": {
"location": "urban downtown street with vintage neon signs",
"time_of_day": "night",
"lighting": "dramatic neon lighting with wet reflections on pavement",
"ambiance": "moody and mysterious film noir atmosphere",
"weather": "heavy rain"
},
"shot": {
"framing": "medium tracking shot from side angle",
"lens": "35mm anamorphic",
"camera_equipment": "ARRI Alexa Mini LF",
"frame_rate": "24fps"
},
"camera_motion": {
"type": "steadicam",
"description": "smooth tracking following subject from side with subtle handheld movement"
},
"style": "cinematic film noir with high contrast and film grain",
"audio": {
"ambient": "rain sounds, distant city traffic, neon buzzing",
"voice_tone": null,
"music_style": "moody jazz noir score with saxophone"
},
"duration_seconds": 8,
"aspect_ratio": "16:9",
"generate_audio": true,
"negative_prompt": ["bright colors", "sunny weather", "modern elements"]
}

text

### Example 3: Nature Documentary

**Input:**
Aerial drone footage of elephants walking across African savanna at sunset

text

**Output:**
{
"subject": {
"description": "Herd of African elephants, including adults and calves",
"action": "walking in single file across open grassland",
"wardrobe": null,
"expression": "peaceful and majestic"
},
"scene": {
"location": "expansive African savanna with acacia trees",
"time_of_day": "golden hour sunset",
"lighting": "warm natural sunlight with long shadows",
"ambiance": "serene and majestic",
"weather": "clear sky with scattered clouds"
},
"shot": {
"framing": "wide aerial establishing shot",
"lens": "24mm wide angle",
"camera_equipment": "DJI Inspire 3 drone",
"frame_rate": "24fps"
},
"camera_motion": {
"type": "crane",
"description": "smooth aerial descent from high altitude following herd"
},
"style": "documentary cinematography with natural colors",
"audio": {
"ambient": "wind rustling grass, distant animal calls, elephant sounds",
"voice_tone": "David Attenborough-style narration",
"music_style": "orchestral documentary score"
},
"duration_seconds": 8,
"aspect_ratio": "16:9",
"generate_audio": true,
"negative_prompt": ["artificial elements", "humans", "buildings"]
}

text

---

## 🔧 Troubleshooting

### Installation Issues

#### Issue: "Python not found"
**Symptoms:**
'python' is not recognized as an internal or external command

text

**Solutions:**
Windows: Reinstall Python with "Add to PATH" checked
Or use: py instead of python
macOS/Linux: Use python3
python3 --version

text

#### Issue: "pip not found"
**Solution:**
Windows
python -m ensurepip --upgrade

macOS/Linux
sudo apt install python3-pip # Ubuntu/Debian
brew install python3 # macOS

text

#### Issue: "ModuleNotFoundError"
**Solution:**
Ensure venv is activated (you should see (venv))
Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

Reinstall dependencies
pip install -r requirements.txt

text

### API & Authentication Issues

#### Issue: "Failed to initialize Gemini"
**Error:**
Failed to initialize Gemini: Error parsing secrets file

text

**Solution:**
1. Check `.streamlit/secrets.toml` format:
GEMINI_API_KEY = "AIzaSyC..." # Must use double quotes!

text
2. Verify no extra spaces or line breaks
3. Ensure file is UTF-8 encoded (not UTF-16 or ANSI)
4. Restart Streamlit app

#### Issue: "Invalid API key"
**Error:**
401 Unauthorized: Invalid API key

text

**Solution:**
1. Verify key is correct at https://makersuite.google.com/app/apikey
2. Check for typos or missing characters
3. Ensure key starts with `AIza`
4. Try generating a new API key

#### Issue: "Quota exceeded"
**Error:**
429 Resource exhausted: Quota exceeded

text

**Solution:**
- Free tier limit: 60 requests/minute
- Wait 60 seconds and try again
- Upgrade to paid plan for higher limits
- Check quota at https://console.cloud.google.com/

### Model & Generation Issues

#### Issue: "Model not found"
**Error:**
404 models/gemini-1.5-flash is not found

text

**Solution:**
Update model name in `gemini_service.py`:
self.model = genai.GenerativeModel('gemini-2.0-flash-exp')

text

#### Issue: "bad argument type for built-in operation"
**Solution:**
Remove enum constraints from function declaration. Use string descriptions instead:
Instead of:
"duration_seconds": {"type": "integer", "enum": }​​

Use:
"duration_seconds": {
"type": "integer",
"description": "Video duration (typically 4, 6, or 8 seconds)"
}

text

#### Issue: "Function calling error"
**Solution:**
1. Verify Gemini model supports function calling
2. Check function declaration syntax
3. Ensure all required fields are present
4. Validate JSON structure

### Streamlit Issues

#### Issue: "Port already in use"
**Error:**
OSError: [Errno 48] Address already in use

text

**Solution:**
Kill process on port 8501
Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F

macOS/Linux
lsof -ti:8501 | xargs kill -9

Or use different port
streamlit run app.py --server.port=8502

text

#### Issue: "Secrets not loading"
**Solution:**
1. Verify `.streamlit/secrets.toml` exists in correct location
2. Check file permissions (should be readable)
3. Restart Streamlit completely (Ctrl+C, then restart)
4. Try `st.secrets` debug:
import streamlit as st
st.write(st.secrets) # Temporary debugging

text

### Deployment Issues

#### Issue: "Repository not found" (Streamlit Cloud)
**Solution:**
1. Ensure repository is **Public** (not Private)
2. Re-authorize Streamlit to access GitHub
3. Check repository name spelling
4. Verify you're logged into correct GitHub account

#### Issue: "Build failed" (Streamlit Cloud)
**Solution:**
1. Check deployment logs for specific error
2. Verify `requirements.txt` has correct versions
3. Ensure `app.py` is in repository root
4. Test locally first: `streamlit run app.py`

#### Issue: "Module not found" (Streamlit Cloud)
**Solution:**
Add missing package to `requirements.txt`:
streamlit==1.38.0
google-generativeai==0.3.2
pydantic==2.5.0

Add any missing packages here
text

### Runtime Issues

#### Issue: Slow generation (>10 seconds)
**Causes & Solutions:**
- Network latency → Use faster internet connection
- Complex prompts → Simplify input
- API rate limiting → Wait and retry
- Model overload → Try during off-peak hours

#### Issue: Incorrect JSON structure
**Solution:**
1. Check Pydantic schema matches requirements
2. Verify function declaration is correct
3. Add more detailed prompts to Gemini
4. Adjust enhanced_prompt template

#### Issue: Missing fields in output
**Solution:**
1. Make fields optional in Pydantic schema
2. Add defaults for optional fields
3. Improve prompt engineering
4. Validate function calling response

### Getting Help

If you can't resolve an issue:

1. **Check logs** - Read terminal output carefully
2. **Search issues** - Check GitHub issues for similar problems
3. **Create issue** - Open new issue with:
   - Error message (full traceback)
   - Steps to reproduce
   - System info (OS, Python version)
   - Screenshots if applicable

4. **Community support:**
   - Streamlit Forum: https://discuss.streamlit.io/
   - Pydantic Discord: https://pydantic.dev/discord
   - Stack Overflow: Tag with `streamlit`, `pydantic`, `gemini-api`

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

### Ways to Contribute

- 🐛 **Report bugs** - Found an issue? Let us know
- 💡 **Suggest features** - Have ideas? Share them
- 📝 **Improve docs** - Help make documentation clearer
- 🔧 **Submit fixes** - Send pull requests
- ⭐ **Star the repo** - Show your support

### Reporting Bugs

1. Check [existing issues](https://github.com/YOUR_USERNAME/veo-schema-api/issues)
2. Create new issue with:
   - **Clear title** - Describe the problem concisely
   - **Steps to reproduce** - Numbered list of steps
   - **Expected behavior** - What should happen
   - **Actual behavior** - What actually happens
   - **Screenshots** - If applicable
   - **Environment** - OS, Python version, etc.

### Suggesting Features

1. Open issue with `enhancement` label
2. Describe the feature clearly
3. Explain use case and benefits
4. Provide examples if possible

### Pull Request Process

1. **Fork the repository**
Click "Fork" on GitHub
git clone https://github.com/YOUR_USERNAME/veo-schema-api.git

text

2. **Create feature branch**
git checkout -b feature/amazing-feature

text

3. **Make changes**
- Follow existing code style
- Add comments where needed
- Update documentation
- Add tests if applicable

4. **Test locally**
streamlit run app.py

Verify everything works
text

5. **Commit changes**
git add .
git commit -m "Add amazing feature: description"

text

6. **Push to GitHub**
git push origin feature/amazing-feature

text

7. **Open Pull Request**
- Go to original repository
- Click "New Pull Request"
- Select your feature branch
- Describe changes clearly
- Link related issues

### Code Style Guidelines

- **Python**: Follow PEP 8
- **Type hints**: Use for function parameters and returns
- **Docstrings**: Add for all functions and classes
- **Comments**: Explain "why", not "what"
- **Naming**: Use descriptive variable names

### Testing

Before submitting PR:
- [ ] App runs without errors locally
- [ ] All features work as expected
- [ ] No secrets committed
- [ ] Documentation updated
- [ ] Code follows style guidelines

---

## 📄 License

This project is licensed under the **MIT License**.

### MIT License

MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

text

### What This Means

✅ **You CAN:**
- Use commercially
- Modify the code
- Distribute
- Private use
- Patent use

❌ **You CANNOT:**
- Hold liable
- Use trademarks

📋 **You MUST:**
- Include license and copyright notice
- State changes made to the code

---

## 🙏 Acknowledgments

Special thanks to:

- **Google Gemini Team** - For the powerful AI model and excellent function calling API
- **Pydantic Team** - For the best data validation library in Python
- **Streamlit Team** - For the amazing framework and free Community Cloud hosting
- **Google Veo Team** - For inspiration and pioneering AI video generation
- **Open Source Community** - For tools, libraries, and inspiration

### Technologies Used

- [Google Gemini 2.0](https://deepmind.google/technologies/gemini/) - AI model
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [Streamlit](https://streamlit.io/) - Web framework
- [Python](https://www.python.org/) - Programming language

---

## 📞 Contact & Support

### Author Information

- **Author**: Your Name
- **GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- **Twitter**: [@yourhandle](https://twitter.com/yourhandle)

### Project Links

- **Repository**: [https://github.com/YOUR_USERNAME/veo-schema-api](https://github.com/YOUR_USERNAME/veo-schema-api)
- **Live Demo**: [https://your-app.streamlit.app](https://your-app.streamlit.app)
- **Issues**: [https://github.com/YOUR_USERNAME/veo-schema-api/issues](https://github.com/YOUR_USERNAME/veo-schema-api/issues)
- **Discussions**: [https://github.com/YOUR_USERNAME/veo-schema-api/discussions](https://github.com/YOUR_USERNAME/veo-schema-api/discussions)

### Getting Support

**For bugs and feature requests:**
Open an issue on GitHub with detailed description

**For questions:**
- GitHub Discussions
- Streamlit Community Forum
- Stack Overflow (tag: `veo-schema-api`)

**For urgent issues:**
Email: your.email@example.com

---

## 🗺️ Roadmap

### Version 1.0 (Current) ✅
- [x] Basic schema enforcement
- [x] Streamlit UI
- [x] Gemini integration
- [x] Example prompts
- [x] JSON export
- [x] Deployment guide

### Version 1.1 (Planned)
- [ ] Batch processing interface
- [ ] Prompt history with local storage
- [ ] Multiple export formats (YAML, XML)
- [ ] Custom schema templates
- [ ] Prompt refinement mode

### Version 2.0 (Future)
- [ ] REST API endpoint
- [ ] Video upload support (extract concepts)
- [ ] Direct Veo API integration
- [ ] Multi-language UI support
- [ ] Advanced cinematography presets
- [ ] Collaborative prompt building

### Version 3.0 (Vision)
- [ ] Chrome extension
- [ ] VS Code extension
- [ ] Figma plugin
- [ ] Video preview generation
- [ ] Community prompt library
- [ ] AI-powered prompt suggestions

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/veo-schema-api?style=social)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/veo-schema-api?style=social)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/veo-schema-api)
![GitHub pull requests](https://img.shields.io/github/issues-pr/YOUR_USERNAME/veo-schema-api)
![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/veo-schema-api)
![GitHub license](https://img.shields.io/github/license/YOUR_USERNAME/veo-schema-api)
![Code size](https://img.shields.io/github/languages/code-size/YOUR_USERNAME/veo-schema-api)

---

## 🎓 Learn More

### Related Resources

**Google Veo:**
- [Veo Documentation](https://deepmind.google/models/veo/)
- [Veo Prompt Guide](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)

**Gemini API:**
- [Function Calling Guide](https://ai.google.dev/gemini-api/docs/function-calling)
- [Gemini Models](https://ai.google.dev/gemini-api/docs/models)

**Pydantic:**
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic V2 Migration](https://docs.pydantic.dev/2.0/migration/)

**Streamlit:**
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Deployment Guide](https://docs.streamlit.io/deploy)

### Tutorials

- [Function Calling with Gemini](https://ai.google.dev/gemini-api/docs/function-calling)
- [Pydantic Validation](https://docs.pydantic.dev/latest/concepts/validators/)
- [Streamlit Best Practices](https://docs.streamlit.io/develop/concepts)

---

## ⚡ Quick Start Summary

1. Clone repository
git clone https://github.com/YOUR_USERNAME/veo-schema-api.git
cd veo-schema-api

2. Create virtual environment
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure API key
mkdir .streamlit
echo 'GEMINI_API_KEY = "your_key_here"' > .streamlit/secrets.toml

5. Run application
streamlit run app.py

6. Open browser
http://localhost:8501
text

---

**Built with ❤️ using Streamlit, Gemini AI, and Pydantic**

**Last Updated**: October 19, 2025  
**Version**: 1.0.0  
**Status**: Active Development

---

## 💬 Feedback

Found this helpful? Please:
- ⭐ Star the repository
- 🐦 Share on Twitter
- 📝 Write a blog post
- 🗣️ Tell your friends

Your feedback helps improve this project!

---

**[Back to Top](#-veo-schema-enforcing-api-unstructured-to-json-normalizer)**
Instructions:

Copy the entire content above (between the triple backticks)

Create a new file named README.md in your project root

Paste the content into the file

Replace these placeholders:

YOUR_USERNAME → Your GitHub username

your.email@example.com → Your email

Your Name → Your actual name

your-app.streamlit.app → Your deployed app URL (after deployment)

Save the file

Commit to GitHub:

bash
git add README.md
git commit -m "Add comprehensive README documentation"
git push
This README is production-ready and follows industry best practices for open-source projects!

github.com favicon
github
https://github.com/othneildrew/Best-README-Template
othneildrew/Best-README-Template: An awesome ...
An awesome README template to jumpstart your projects! - GitHub - othneildrew/Best-README-Template: An awesome README template to jumpstart your projects!
github.com favicon
github
https://github.com/python-project-templates
Python Project Templates
Python, C++, Rust, JavaScript, Jupyter, and more. Python Project Templates has 22 repositories available. Follow their code on GitHub.
realpython.com favicon
realpython
https://realpython.com/readme-python-project/
Creating Great README Files for Your Python Projects
In this tutorial, you'll learn how to create, organize, and format high-quality README files for your Python projects.
Related
Provide my project type and main features for a tailored README
Generate a README.md for a Python package with setup instructions
Create a README.md for a Streamlit app including deploy steps
Add badges, license, and contribution guidelines to the README
Produce a minimal README.md and a more detailed extended version

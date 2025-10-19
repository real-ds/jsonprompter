from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class AspectRatio(str, Enum):
    """Supported aspect ratios for Veo"""
    WIDESCREEN = "16:9"
    VERTICAL = "9:16"

class Duration(int, Enum):
    """Supported durations in seconds"""
    SHORT = 4
    MEDIUM = 6
    LONG = 8

class CameraMotion(BaseModel):
    """Camera movement specifications"""
    type: str = Field(..., description="Type of camera motion: dolly, crane, orbit, steadicam, handheld, static")
    description: Optional[str] = Field(None, description="Detailed camera movement description")

class ShotComposition(BaseModel):
    """Shot framing and technical specifications"""
    framing: str = Field(..., description="Shot framing: wide shot, medium shot, close-up, extreme close-up")
    lens: Optional[str] = Field(None, description="Lens specification: 24mm, 50mm, 85mm, etc.")
    camera_equipment: Optional[str] = Field(None, description="Camera equipment: ARRI Alexa, RED, etc.")
    frame_rate: Optional[str] = Field("24fps", description="Frame rate specification")

class Subject(BaseModel):
    """Subject/character specifications"""
    description: str = Field(..., description="Detailed description of the subject/character")
    action: str = Field(..., description="What the subject is doing")
    wardrobe: Optional[str] = Field(None, description="Clothing and appearance details")
    expression: Optional[str] = Field(None, description="Facial expression or emotion")

class Scene(BaseModel):
    """Scene environment specifications"""
    location: str = Field(..., description="Physical location or setting")
    time_of_day: str = Field(..., description="Time: golden hour, night, midday, etc.")
    lighting: str = Field(..., description="Lighting conditions: natural, studio, dramatic, etc.")
    ambiance: Optional[str] = Field(None, description="Overall mood and atmosphere")
    weather: Optional[str] = Field(None, description="Weather conditions if relevant")

class Audio(BaseModel):
    """Audio specifications"""
    ambient: Optional[str] = Field(None, description="Background environmental sounds")
    voice_tone: Optional[str] = Field(None, description="Voice characteristics if dialogue present")
    music_style: Optional[str] = Field(None, description="Background music style")

class VeoPromptSchema(BaseModel):
    """Complete Veo video generation prompt schema"""
    
    # Core elements (required)
    subject: Subject = Field(..., description="The main subject of the video")
    scene: Scene = Field(..., description="Scene environment and setting")
    
    # Technical specifications
    shot: ShotComposition = Field(..., description="Shot composition and framing")
    camera_motion: CameraMotion = Field(..., description="Camera movement specifications")
    
    # Optional enhancements
    style: str = Field(..., description="Visual style: cinematic, documentary, horror, animated, etc.")
    audio: Optional[Audio] = Field(None, description="Audio specifications")
    
    # Generation parameters
    duration_seconds: Duration = Field(Duration.LONG, description="Video duration in seconds")
    aspect_ratio: AspectRatio = Field(AspectRatio.WIDESCREEN, description="Video aspect ratio")
    generate_audio: bool = Field(True, description="Whether to generate audio")
    
    # Advanced controls
    negative_prompt: Optional[List[str]] = Field(None, description="Elements to avoid: text overlays, artifacts, etc.")
    
    class Config:
        json_schema_extra = {
            "example": {
                "subject": {
                    "description": "A young woman in her 20s with long dark hair",
                    "action": "walking confidently down a city street",
                    "wardrobe": "casual denim jacket and white sneakers",
                    "expression": "smiling and looking ahead"
                },
                "scene": {
                    "location": "urban downtown street with modern architecture",
                    "time_of_day": "golden hour",
                    "lighting": "warm natural sunlight",
                    "ambiance": "vibrant and energetic",
                    "weather": "clear sky"
                },
                "shot": {
                    "framing": "medium tracking shot",
                    "lens": "85mm",
                    "camera_equipment": "ARRI Alexa Mini LF",
                    "frame_rate": "24fps"
                },
                "camera_motion": {
                    "type": "steadicam",
                    "description": "smooth tracking alongside subject with slight handheld bounce"
                },
                "style": "cinematic with film-emulated color grading",
                "audio": {
                    "ambient": "city traffic and distant conversations",
                    "voice_tone": "natural and confident"
                },
                "duration_seconds": 8,
                "aspect_ratio": "16:9",
                "generate_audio": True,
                "negative_prompt": ["text overlays", "captions", "distorted faces"]
            }
        }

class UnstructuredInput(BaseModel):
    """Input model for unstructured text"""
    text: str = Field(..., description="Unstructured text description of desired video")
    
class VeoPromptResponse(BaseModel):
    """API response model"""
    status: str
    structured_prompt: VeoPromptSchema
    raw_text_input: str

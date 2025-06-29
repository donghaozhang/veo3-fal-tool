# AI Video Generation Project

This project provides comprehensive Python implementations for generating videos using multiple AI platforms and models. It's organized into specialized folders for different video generation services.

## 🎬 Available Implementations

### 1. Google Veo Video Generation (`veo3_video_generation/`)
- **Models**: Veo 2.0 (stable) and Veo 3.0 (preview)
- **Features**: Text-to-video, Image-to-video generation
- **Quality**: High-resolution, cinematic quality
- **Setup**: Requires Google Cloud authentication and configuration

### 2. FAL AI Dual-Model Generation (`fal_video_generation/`)
- **Models**: MiniMax Hailuo-02 and Kling Video 2.1
- **Features**: Production-ready API, dual model support, cost-conscious testing
- **Quality**: 768p (Hailuo) and high-quality (Kling)
- **Setup**: Simple API key authentication
- **⚠️ Cost Warning**: Video generation costs money (~$0.02-0.05 per video)

### 3. FAL AI Avatar Generation (`fal_avatar_generation/`)
- **Model**: AI Avatar Single-Text (MultiTalk)
- **Features**: Text-to-speech avatar videos with lip-sync
- **Quality**: Talking avatars with natural expressions
- **Voices**: 20 different voice options
- **Setup**: Simple API key authentication
- **⚠️ Cost Warning**: Avatar generation costs money (~$0.02-0.05 per video)

### 4. ✨ **NEW!** ElevenLabs Text-to-Speech Package (`text_to_speech/`)
- **Features**: Comprehensive modular TTS package with OpenRouter AI integration
- **Architecture**: Recently refactored from monolithic to professional modular structure
- **Capabilities**: Voice control, dialogue generation, timing control, 3000+ voices
- **Pipeline**: Complete AI content generation (OpenRouter → ElevenLabs TTS)
- **Models**: Support for top 10 OpenRouter models (Claude, Gemini, DeepSeek, etc.)
- **Setup**: Simple API key authentication (ElevenLabs + OpenRouter)

## 📁 Project Structure

```
veo3-video-generation/
├── README.md                           # This overview
├── CLAUDE.md                          # Claude Code project instructions
├── requirements.txt                    # Global dependencies
├── 
├── veo3_video_generation/             # Google Veo Implementation
│   ├── veo_video_generation.py        # Main Veo implementation
│   ├── demo.py                        # Interactive Veo demo
│   ├── test_veo.py                    # Comprehensive test suite
│   ├── fix_permissions.py             # GCP permissions helper
│   ├── README.md                      # Veo-specific documentation
│   └── requirements.txt               # Veo dependencies
│
├── fal_avatar_generation/             # FAL AI Avatar Implementation
│   ├── fal_avatar_generator.py        # Avatar video generator class
│   ├── demo.py                        # Cost-conscious interactive demo
│   ├── test_setup.py                  # FREE environment tests
│   ├── test_generation.py             # PAID avatar generation tests
│   ├── test_official_example.py       # Official FAL examples test
│   ├── README.md                      # Avatar generation documentation
│   └── requirements.txt               # Avatar dependencies
│
├── fal_text_to_image/                 # FAL AI Text-to-Image Implementation
│   ├── fal_text_to_image_generator.py # Multi-model image generator class
│   ├── demo.py                        # Interactive image generation demo
│   ├── test_setup.py                  # FREE environment validation
│   ├── test_generation.py             # PAID image generation tests
│   ├── README.md                      # Text-to-image documentation
│   ├── requirements.txt               # Text-to-image dependencies
│   ├── output/                        # Generated images output
│   └── test_output/                   # Test images output
│
├── fal_image_to_image/                # FAL AI Image-to-Image Implementation
│   ├── fal_image_to_image/            # Main package directory
│   │   ├── __init__.py                # Package initialization
│   │   ├── generator.py               # Core image modification logic
│   │   ├── models/                    # Model implementations
│   │   │   ├── __init__.py
│   │   │   ├── base.py                # Base model interface
│   │   │   ├── photon.py              # Luma Photon Flash model
│   │   │   ├── seededit.py            # SeedEdit model
│   │   │   └── kontext.py             # Kontext model
│   │   ├── config/                    # Configuration management
│   │   │   ├── __init__.py
│   │   │   └── constants.py           # Model constants and settings
│   │   └── utils/                     # Utility functions
│   │       ├── __init__.py
│   │       ├── file_utils.py          # File handling utilities
│   │       └── validators.py          # Input validation
│   ├── examples/                      # Usage examples and demos
│   │   ├── __init__.py
│   │   ├── basic_usage.py             # Basic usage examples
│   │   ├── demo.py                    # Interactive demo
│   │   ├── model_comparison.py        # Compare different models
│   │   ├── output/                    # Example output directory
│   │   └── test_output/               # Test output directory
│   ├── tests/                         # Test suite
│   │   ├── __init__.py
│   │   ├── test_setup.py              # FREE environment tests
│   │   ├── test_generation.py         # PAID generation tests
│   │   ├── test_package_structure.py  # Package structure validation
│   │   └── test_models/               # Model-specific tests
│   ├── docs/                          # Documentation
│   │   ├── API_REFERENCE.md           # API documentation
│   │   └── README_SEEDEDIT.md         # SeedEdit model documentation
│   ├── input/                         # Input images for testing
│   ├── output/                        # Generated images output
│   ├── setup.py                       # Package installation
│   ├── requirements.txt               # Image-to-image dependencies
│   ├── README.md                      # Image-to-image documentation
│   └── archive/                       # Legacy implementations
│
├── fal_image_to_video/                # FAL AI Image-to-Video Implementation
│   ├── fal_image_to_video_generator.py # Image-to-video generator class
│   ├── demo.py                        # Cost-conscious interactive demo
│   ├── test_fal_ai.py                 # Cost-conscious test suite
│   ├── test_api_only.py               # FREE API connection test
│   ├── README.md                      # Image-to-video documentation
│   ├── COST_CONSCIOUS_TESTING.md      # Cost protection guide
│   └── requirements.txt               # Image-to-video dependencies
│
├── text_to_speech/                    # ✨ Modular TTS Package
│   ├── __init__.py                    # Package initialization
│   ├── README.md                      # TTS package documentation
│   ├── MIGRATION_GUIDE.md             # Migration from old structure
│   ├── setup.py                       # Package installation
│   ├── requirements.txt               # TTS dependencies
│   ├── models/                        # Data models and enums
│   │   ├── __init__.py
│   │   ├── common.py                  # Common data models
│   │   └── pipeline.py                # Pipeline models
│   ├── tts/                           # Core TTS functionality
│   │   ├── __init__.py
│   │   ├── controller.py              # Main TTS controller
│   │   ├── voice_manager.py           # Voice management
│   │   └── audio_processor.py         # Audio processing utilities
│   ├── pipeline/                      # OpenRouter AI integration
│   │   ├── __init__.py
│   │   └── core.py                    # AI content generation pipeline
│   ├── utils/                         # Utility functions
│   │   ├── __init__.py
│   │   ├── validators.py              # Input validation
│   │   ├── file_manager.py            # File management
│   │   └── api_helpers.py             # API helper functions
│   ├── config/                        # Configuration management
│   │   ├── __init__.py
│   │   ├── defaults.py                # Default settings
│   │   ├── voices.py                  # Voice configurations
│   │   └── models.py                  # Model configurations
│   ├── examples/                      # Usage examples
│   │   ├── __init__.py
│   │   └── basic_usage.py             # Basic TTS examples
│   ├── cli/                           # Command line tools
│   │   ├── __init__.py
│   │   ├── interactive.py             # Interactive pipeline
│   │   └── quick_start.py             # Quick start demo
│   ├── dialogue/                      # Dialogue generation (placeholder)
│   │   └── __init__.py
│   └── output/                        # Generated audio files
│
├── video_tools/                       # Video Processing Utilities
│   ├── README.md                      # Video tools documentation
│   ├── video_audio_utils.py           # Audio processing utilities
│   ├── image_modify_verify.py         # Image modification and verification
│   ├── real_video_examples.py         # Real video processing examples
│   ├── requirements_gemini.txt        # Gemini-specific requirements
│   ├── video_utils/                   # Core video processing modules
│   │   ├── __init__.py
│   │   ├── core.py                    # Core video processing
│   │   ├── commands.py                # Command utilities
│   │   ├── interactive.py             # Interactive video tools
│   │   ├── file_utils.py              # File management utilities
│   │   ├── video_processor.py         # Video processing engine
│   │   ├── audio_processor.py         # Audio processing engine
│   │   ├── subtitle_generator.py      # Subtitle generation
│   │   ├── video_understanding.py     # Video analysis and understanding
│   │   ├── video_commands.py          # Video manipulation commands
│   │   ├── audio_commands.py          # Audio manipulation commands
│   │   ├── subtitle_commands.py       # Subtitle commands
│   │   ├── whisper_commands.py        # Whisper integration
│   │   └── ai_analysis_commands.py    # AI-powered analysis
│   ├── docs/                          # Documentation
│   │   ├── API_REFERENCE.md           # API documentation
│   │   ├── BETTER_IMPLEMENTATION_ANALYSIS.md # Implementation analysis
│   │   ├── COMMAND_LINE_EXAMPLES.md   # Command line examples
│   │   └── GEMINI_SETUP.md            # Gemini setup instructions
│   ├── input/                         # Input files for testing
│   ├── output/                        # Processed output files
│   └── tests/                         # Test suite
│       ├── test_env_setup.py          # Environment setup tests
│       ├── test_image_workflow.py     # Image workflow tests
│       ├── test_subtitles.py          # Subtitle generation tests
│       └── test_video_understanding.py # Video understanding tests
```

## 🚀 Quick Start

### Option 1: Google Veo (High-Quality, Complex Setup)

```bash
cd veo3_video_generation
pip install -r requirements.txt

# Configure Google Cloud authentication
gcloud auth login
gcloud auth application-default login
gcloud config set project your-project-id

# Update configuration in .env file
# PROJECT_ID=your-project-id
# OUTPUT_BUCKET_PATH=gs://your-bucket/veo_output/

# Run demo
python demo.py

# Or run tests
python test_veo.py
```

### Option 2: FAL AI (Simple Setup, Production Ready)

```bash
cd fal_video_generation
pip install -r requirements.txt

# Configure API key in .env file
# FAL_KEY=your-fal-api-key

# Test setup first (FREE)
python test_api_only.py

# Run demo (costs money - has confirmation prompts)
python demo.py

# Or run specific model tests (costs money)
python test_fal_ai.py --hailuo    # ~$0.02-0.05
python test_fal_ai.py --kling     # ~$0.02-0.05
```

### Option 3: ✨ **NEW!** Text-to-Speech Package (Professional TTS + AI)

```bash
cd text_to_speech
pip install -r requirements.txt

# Configure API keys in .env file (or environment variables)
# ELEVENLABS_API_KEY=your-elevenlabs-key
# OPENROUTER_API_KEY=your-openrouter-key

# Basic TTS usage
python examples/basic_usage.py

# Interactive pipeline (AI content generation → TTS)
python cli/interactive.py

# Quick start demo
python cli/quick_start.py

# Advanced usage examples
python -c "
from text_to_speech import ElevenLabsTTSController
tts = ElevenLabsTTSController('your-api-key')
tts.text_to_speech_with_timing_control(
    text='Hello! This is the new modular TTS package.',
    voice_name='rachel',
    output_file='output/welcome.mp3'
)
"
```

## 🔧 Setup Requirements

### Google Veo Requirements
- Google Cloud Project with Vertex AI API enabled
- Google Cloud Storage bucket
- Proper authentication (gcloud CLI)
- Python 3.8+
- Veo 3.0 requires allowlist approval

### FAL AI Requirements
- FAL AI API key (from fal.ai)
- Python 3.8+
- Internet connection

### Text-to-Speech Package Requirements
- ElevenLabs API key (from elevenlabs.io)
- OpenRouter API key (from openrouter.ai) - for AI content generation
- Python 3.8+
- Internet connection
- **New Modular Architecture**: Recently refactored for professional development

## 📊 Feature Comparison

### Video Generation Models

| Feature | Google Veo 2.0 | Google Veo 3.0 | FAL Hailuo-02 | FAL Kling 2.1 |
|---------|----------------|----------------|---------------|----------------|
| **Resolution** | High | Higher | 768p | High-quality |
| **Setup Complexity** | Complex | Complex | Simple | Simple |
| **Authentication** | Google Cloud | Google Cloud | API Key | API Key |
| **Access** | Generally Available | Preview/Allowlist | Public API | Public API |
| **Generation Time** | 2-10 min | 2-10 min | 1-3 min | 1-3 min |
| **Best For** | Cinematic quality | Latest features | Quick prototyping | High-quality production |

### ✨ Text-to-Speech Package Features

| Feature | Description | Status |
|---------|-------------|---------|
| **Architecture** | Modular package structure (15+ focused modules) | ✅ Recently refactored |
| **Voice Library** | 3000+ ElevenLabs voices + popular presets | ✅ Comprehensive |
| **AI Integration** | OpenRouter (Claude, Gemini, DeepSeek, etc.) | ✅ Top 10 models |
| **Pipeline** | Description → AI Content → Speech | ✅ End-to-end |
| **Features** | Timing control, dialogue, voice cloning | ✅ Professional |
| **Setup** | Simple API keys (ElevenLabs + OpenRouter) | ✅ Easy |

## 🎯 Use Cases

### Choose Google Veo When:
- You need the highest quality video generation
- You have Google Cloud infrastructure
- You're building enterprise applications
- Quality is more important than speed

### Choose FAL AI When:
- You want quick setup and testing
- You need reliable production API
- You want to compare multiple models
- You prefer simple API key authentication

### Choose Text-to-Speech Package When:
- You need professional voice synthesis
- You want AI-generated content with speech
- You need multi-speaker dialogue generation
- You want a complete content creation pipeline
- You prefer modular, maintainable code architecture

## 🛠️ Development Features

### Google Veo Features
- ✅ Text-to-video generation
- ✅ Image-to-video generation
- ✅ Multiple model support (2.0 + 3.0)
- ✅ Local image processing
- ✅ Automatic GCS upload/download
- ✅ Comprehensive error handling
- ✅ Interactive demo with model selection
- ✅ Full test suite with comparison

### FAL AI Features
- ✅ Dual-model architecture (Hailuo + Kling)
- ✅ Universal methods with full endpoint names
- ✅ Model-specific optimization
- ✅ Cost-conscious interactive demo with confirmation prompts
- ✅ Cost-conscious testing framework with FREE options
- ✅ Production-ready error handling
- ✅ Automatic video download
- ✅ Model performance comparison
- ⚠️ Cost protection with explicit user confirmation required

### ✨ Text-to-Speech Package Features
- ✅ **Modular Architecture**: 15+ focused modules (150-300 lines each)
- ✅ **Professional Package**: setup.py, proper imports, clean structure
- ✅ **Voice Control**: 3000+ voices, popular presets, custom cloning
- ✅ **AI Integration**: OpenRouter (Claude, Gemini, DeepSeek, etc.)
- ✅ **Complete Pipeline**: Description → AI Content → Speech
- ✅ **Multi-Speaker Dialogue**: Emotional tags, voice pairing
- ✅ **Timing Control**: Speed, pauses, natural speech patterns
- ✅ **Utilities**: Validation, file management, error handling
- ✅ **Configuration**: Voice presets, model settings, defaults
- ✅ **Examples & CLI**: Interactive tools, usage examples
- ✅ **Backward Compatible**: Existing code works with minimal changes
- 📚 **Migration Guide**: Complete transition documentation

## 📖 Documentation

Each implementation has its own detailed documentation:

- **Google Veo**: See [`veo3_video_generation/README.md`](veo3_video_generation/README.md)
- **FAL AI Video**: See [`fal_video_generation/README.md`](fal_video_generation/README.md)
- **FAL AI Avatar**: See [`fal_avatar_generation/README.md`](fal_avatar_generation/README.md)
- **✨ Text-to-Speech**: See [`text_to_speech/README.md`](text_to_speech/README.md)
  - **Migration Guide**: [`text_to_speech/MIGRATION_GUIDE.md`](text_to_speech/MIGRATION_GUIDE.md)
  - **Setup Instructions**: [`text_to_speech/setup.py`](text_to_speech/setup.py)

## 🧪 Testing

### Test Google Veo Implementation
```bash
cd veo3_video_generation

# Basic tests
python test_veo.py

# Test Veo 3.0 specifically
python test_veo.py --veo3

# Compare both models
python test_veo.py --compare

# Full comprehensive tests
python test_veo.py --full
```

### Test FAL AI Implementation

⚠️ **Cost Warning**: Video generation tests cost money! Always start with FREE tests.

```bash
cd fal_video_generation

# FREE Tests (no cost)
python test_api_only.py              # API connection test only
python test_fal_ai.py                # Setup validation only

# Paid Tests (generate real videos)
python test_fal_ai.py --hailuo       # Test Hailuo model (~$0.02-0.05)
python test_fal_ai.py --kling        # Test Kling model (~$0.02-0.05)
python test_fal_ai.py --compare      # Test both models (~$0.04-0.10)
```

### Test Text-to-Speech Package

✅ **No Cost**: Text-to-speech testing supports dummy API keys for structure validation.

```bash
cd text_to_speech

# Test package structure (FREE - no API calls)
python -c "
import sys
sys.path.append('..')
from text_to_speech import ElevenLabsTTSController
print('✅ Package imports working!')
"

# Test with dummy keys (FREE - no API calls)
python examples/basic_usage.py       # Basic TTS examples

# Test individual modules
python -c "
from text_to_speech.utils.validators import validate_text_input
print('✅ Utilities working!')
"

# Interactive demos (requires real API keys)
python cli/interactive.py            # Interactive pipeline
python cli/quick_start.py           # Quick start demo
```

## 🎮 Interactive Demos

All implementations include interactive demos:

```bash
# Google Veo Demo
cd veo3_video_generation && python demo.py

# FAL AI Video Demo (costs money - has confirmation prompts)
cd fal_video_generation && python demo.py

# FAL AI Avatar Demo (costs money - has confirmation prompts)
cd fal_avatar_generation && python demo.py

# ✨ Text-to-Speech Interactive Pipeline
cd text_to_speech && python cli/interactive.py

# ✨ Text-to-Speech Quick Start Demo
cd text_to_speech && python cli/quick_start.py
```

The demos provide:
- **Video Generation**: Model selection menus with cost warnings
- **Video Features**: Pre-configured test prompts, image-to-video testing
- **Cost Protection**: Confirmation prompts before generating videos
- **✨ TTS Pipeline**: AI content generation → speech conversion
- **✨ TTS Features**: Voice selection, timing control, multi-speaker dialogue
- **Configuration Validation**: Setup verification for all platforms

## 🔍 Troubleshooting

### Common Issues

#### Google Veo Issues
- **"Project not allowlisted"**: Use Veo 2.0 or request Veo 3.0 access
- **Permission denied**: Check GCS bucket permissions
- **Authentication failed**: Run `gcloud auth application-default login`

#### FAL AI Issues
- **Invalid API key**: Check your FAL_KEY in .env file
- **Rate limiting**: Wait between requests or upgrade plan
- **Model not available**: Try alternative model
- **Unexpected charges**: Always use FREE tests first (`test_api_only.py`)

#### ✨ Text-to-Speech Issues
- **Import errors**: Ensure `PYTHONPATH` includes project root or install with `pip install -e .`
- **Invalid API key**: Check `ELEVENLABS_API_KEY` and `OPENROUTER_API_KEY` in environment
- **Missing List import**: Fixed in latest version (use `from typing import List`)
- **Old import errors**: Use migration guide to update from monolithic structure
- **Package structure**: Use new modular imports (see `MIGRATION_GUIDE.md`)

### Getting Help

1. Check the specific README for your implementation
2. Review the test suite output for diagnostic information
3. Run the demo to validate your setup
4. Check the troubleshooting sections in each implementation's README

## ⚠️ Cost Protection

**IMPORTANT**: FAL AI video generation costs money (~$0.02-0.05 per video). This project includes cost protection measures:

- **FREE tests available**: Use `test_api_only.py` for setup validation
- **Cost warnings**: All paid operations show cost estimates
- **Confirmation prompts**: User must explicitly confirm before generating videos
- **Model-specific testing**: Test individual models to avoid unnecessary costs

**Always start with FREE tests before running paid video generation!**

## 🚧 Development Status

- ✅ **Google Veo**: Production ready with comprehensive testing
- ✅ **FAL AI Video**: Production ready with cost-conscious dual-model support
- ✅ **FAL AI Avatar**: Production ready with text-to-speech integration
- ✅ **✨ Text-to-Speech**: Recently refactored to modular architecture - fully functional
  - 🆕 **Architecture**: Transformed from 3 monolithic files (2,500+ lines) to 15+ focused modules
  - ✅ **Testing**: Comprehensive test suite with import validation
  - ✅ **Migration**: Complete migration guide and backward compatibility
  - ✅ **Professional**: Setup.py, proper package structure, CLI tools
- 🔄 **Future**: Additional model integrations and enhanced pipeline features planned

## 📝 License

This project is open source. Please check individual implementation folders for specific licensing information.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Update documentation
5. Submit a pull request

## 📚 Resources

### Google Veo Resources
- [Veo API Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation)
- [Google GenAI SDK](https://github.com/google/generative-ai-python)
- [Vertex AI Console](https://console.cloud.google.com/vertex-ai)

### FAL AI Resources
- [FAL AI Platform](https://fal.ai/)
- [MiniMax Hailuo Documentation](https://fal.ai/models/fal-ai/minimax-video-01)
- [Kling Video 2.1 Documentation](https://fal.ai/models/fal-ai/kling-video/v2.1/standard/image-to-video/api)
- [FAL AI Avatar Documentation](https://fal.ai/models/fal-ai/avatar-video)

### ✨ Text-to-Speech Resources
- [ElevenLabs API Documentation](https://elevenlabs.io/docs/capabilities/text-to-speech)
- [OpenRouter Platform](https://openrouter.ai/)
- [ElevenLabs Voice Library](https://elevenlabs.io/app/speech-synthesis/text-to-speech)
- [Text-to-Dialogue Documentation](https://elevenlabs.io/docs/cookbooks/text-to-dialogue)
- [Package Migration Guide](text_to_speech/MIGRATION_GUIDE.md)

---

**🎬 Happy Creating!** Choose the implementation that best fits your needs and start creating amazing AI-generated videos and professional text-to-speech content! 🎙️ 
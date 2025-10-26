# 🧠 PARTH - Personal Advanced Reasoning & Task Handling Intelligence

<div align="center">

![PARTH Logo](assets/logo.png)

**The Ultimate Free & Open-Source JARVIS-Level AI Assistant**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-green.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20iOS%20%7C%20Windows%20%7C%20Linux%20%7C%20macOS-orange.svg)](#)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 🌟 What is PARTH?

**PARTH** is a revolutionary, completely **free** and **open-source** AI assistant system designed to work exactly like **JARVIS** from Iron Man. It can:

- 🎙️ **Listen and speak** naturally with human-like conversation
- 📱 **Control all your devices** (phone, PC, laptop, smart home)
- 🧠 **Think and reason** using 75+ state-of-the-art AI models
- 🤖 **Perform any task** from simple searches to complex automation
- 🔒 **100% private** - all processing happens locally on your device
- 💰 **Completely free** - no subscriptions, no API costs, no limits

### Built For

- **Primary User:** Prabhu (and anyone who wants a personal AI)
- **Primary Device:** Poco X6 Pro (12GB RAM, MediaTek Dimensity 8300 Ultra)
- **Universal:** Works on Android, iOS, Windows, Linux, macOS

---

## ✨ Features

### 🗣️ Natural Communication

- **Voice Interface:** Wake word activation ("Hey Parth"), continuous listening
- **Speech Recognition:** Whisper AI (98+ languages, highly accurate)
- **Text-to-Speech:** Chatterbox + Piper TTS (natural, emotional voices)
- **Chat Interface:** Rich terminal UI and web interface
- **Human-like:** Shows appropriate emotions, understands context, natural conversation

### 🎯 Intelligence & Reasoning

**75+ AI Models Orchestrated:**
- **Reasoning:** Meta Llama 3.1, Mistral, Phi-3, Qwen, Yi, Gemma, Falcon
- **Code Generation:** CodeLlama, DeepSeek-Coder, WizardCoder, StarCoder
- **Vision:** LLaVA, CLIP, Stable Diffusion, ControlNet, SAM
- **Multi-Agent:** AutoGPT, MetaGPT, CrewAI, LangChain, BabyAGI
- **Specialized:** Document parsing, music generation, voice cloning, and more

### 📱 Device Control

**Android (via Termux):**
- Phone calls, SMS, emails, notifications
- Camera control, file management
- App automation, system settings
- Screen control, sensor access

**Desktop (Windows/Linux/macOS):**
- Full system automation
- Browser control (Selenium/Playwright)
- File operations, process management
- Application control, shortcuts

**iOS:**
- Shortcuts integration
- App automation
- iCloud sync

### 🤖 Task Execution

- **Web Search & Research:** Multi-source aggregation and summarization
- **Code Generation:** Full-stack apps from description or GitHub repos
- **Content Creation:** Writing, images, videos, music
- **Automation:** Complex workflows, scheduled tasks
- **Learning:** Personalized courses and skill development
- **GitHub Integration:** Auto-analyze, fix, deploy, create PRs

### 🧠 Memory & Learning

- **Short-term Memory:** Maintains conversation context
- **Long-term Memory:** Remembers preferences, past interactions
- **Continuous Learning:** Adapts to your style and needs
- **Personalization:** Customizes everything to your preferences

---

## 🚀 Installation

### 📱 Android (Termux) - Recommended for Poco X6 Pro

Detailed guide: [docs/deployment/TERMUX_INSTALLATION.md](docs/deployment/TERMUX_INSTALLATION.md)

**Quick start:**

```bash
# 1. Install Termux and Termux:API from F-Droid
# 2. Open Termux and run:

pkg update -y && pkg upgrade -y
pkg install -y git python nodejs-lts termux-api
termux-setup-storage

# 3. Clone PARTH
git clone https://github.com/[YOUR-USERNAME]/parth-ai.git
cd parth-ai

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download AI models
python setup_models.py --device android --ram 12GB

# 6. Run PARTH
python parth.py
```

### 💻 Desktop (Windows/Linux/macOS)

**Linux/macOS:**
```bash
git clone https://github.com/[YOUR-USERNAME]/parth-ai.git
cd parth-ai
pip3 install -r requirements.txt
python3 setup_models.py --device desktop
python3 parth.py
```

**Windows:**
```powershell
git clone https://github.com/[YOUR-USERNAME]/parth-ai.git
cd parth-ai
pip install -r requirements.txt
python setup_models.py --device desktop
python parth.py
```

### ☁️ Cloud Deployment

**Hugging Face Spaces:**
- Fork this repo
- Create new Space on huggingface.co
- Connect to GitHub repo
- Space builds automatically

**Google Colab:** [Open in Colab](https://colab.research.google.com/github/[YOUR-USERNAME]/parth-ai/blob/main/notebooks/parth_colab.ipynb)

---

## 💬 Usage

### Basic Chat

```bash
python parth.py
```

Then just talk to Parth!

```
Prabhu: Hey Parth, what's the weather today?
Parth: Good morning, Prabhu! It's currently 24°C and sunny...

Prabhu: Create a to-do list app for me
Parth: Sure! I'll create a full-stack to-do app with React and Node.js...
```

### Voice Mode

```bash
python parth.py --voice
```

Say **"Hey Parth"** or **"Parth"** to activate, then speak naturally!

### Web Interface

```bash
python parth.py --mode web --port 8080
```

Open browser to `http://localhost:8080`

### Advanced Options

```bash
# Performance mode (uses more resources)
python parth.py --performance-mode

# Smaller models (saves memory)
python parth.py --model-size small

# Custom configuration
python parth.py --config my_config.yaml

# Debug mode
python parth.py --debug

# Background mode
python parth.py --background
```

---

## 📖 Documentation

### User Guides

- [📱 Termux Installation](docs/deployment/TERMUX_INSTALLATION.md) - Complete Android setup
- [💻 Desktop Installation](docs/deployment/DESKTOP_INSTALLATION.md) - Windows/Linux/macOS
- [☁️ Cloud Deployment](docs/deployment/CLOUD_DEPLOYMENT.md) - Hugging Face, Google Cloud
- [🎙️ Voice Setup](docs/guides/VOICE_SETUP.md) - Voice features and wake words
- [📱 Device Control](docs/guides/DEVICE_CONTROL.md) - How to control your devices
- [🤖 Commands & Tasks](docs/guides/COMMANDS.md) - What PARTH can do

### Technical Documentation

- [🧠 System Prompt](PARTH_SYSTEM_PROMPT.md) - Complete system specification
- [🏗️ Architecture](docs/technical/ARCHITECTURE.md) - System design and components
- [🔌 API Reference](docs/technical/API.md) - Programming interface
- [🤖 Model Integration](docs/technical/MODELS.md) - How AI models work together
- [🔧 Configuration](docs/technical/CONFIGURATION.md) - Customize PARTH

### Development

- [🛠️ Contributing Guide](CONTRIBUTING.md) - How to contribute
- [🐛 Bug Reports](https://github.com/[YOUR-USERNAME]/parth-ai/issues) - Report issues
- [💡 Feature Requests](https://github.com/[YOUR-USERNAME]/parth-ai/discussions) - Suggest features

---

## 🎯 Examples

### Everyday Tasks

```
Prabhu: Parth, remind me to call mom at 6 PM
Parth: Reminder set for 6 PM today. I'll notify you!

Prabhu: What's trending on Twitter?
Parth: Here are today's top trends: [analyzes and summarizes]

Prabhu: Book me a cab to the airport
Parth: Opening Uber with destination set to airport...
```

### Development

```
Prabhu: Create a REST API for user authentication
Parth: Creating Express.js API with JWT authentication...
[Generates complete working code]

Prabhu: Fix the bug in my GitHub repo
Parth: Analyzing repository... Found issue in line 45...
[Creates fix and submits PR]
```

### Creative

```
Prabhu: Generate a logo for "TechStart"
Parth: Creating modern tech logo options...
[Shows 4 logo variations]

Prabhu: Write a poem about AI
Parth: [Generates creative poem]
```

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md)

**Ways to contribute:**
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests
- 🌐 Translate to other languages
- 🎨 Design improvements

---

## 🏆 Why PARTH?

| Feature | PARTH | Other AI Assistants |
|---------|-------|---------------------|
| **Cost** | 100% Free Forever | $20-200/month |
| **Privacy** | 100% Local | Cloud-based |
| **Device Control** | Full Access | Limited/None |
| **Customization** | Unlimited | Restricted |
| **Open Source** | Yes | No |
| **Offline Mode** | Yes | No |
| **Multi-Model** | 75+ Models | Single Model |
| **Platform** | All Platforms | Limited |

---

## 📊 System Requirements

### Minimum (Small Models)

- **RAM:** 6GB
- **Storage:** 10GB free
- **Platform:** Android 8+, Windows 10+, Linux, macOS 10.15+

### Recommended (Medium Models)

- **RAM:** 12GB (Poco X6 Pro optimal)
- **Storage:** 20GB free
- **Processor:** 8-core
- **GPU:** Optional (NVIDIA/AMD for faster processing)

### Optimal (Large Models)

- **RAM:** 16GB+
- **Storage:** 50GB+ free
- **GPU:** NVIDIA RTX 3060 or better
- **Processor:** High-performance CPU

---

## 🔒 Privacy & Security

- ✅ **100% Local Processing** - No data sent to cloud
- ✅ **Encrypted Storage** - All data encrypted at rest
- ✅ **No Telemetry** - No tracking or analytics
- ✅ **Open Source** - Fully auditable code
- ✅ **User Control** - You own all your data

---

## 📜 License

Apache License 2.0 - See [LICENSE](LICENSE) file

**This means:**
- ✅ Free to use, modify, distribute
- ✅ Commercial use allowed
- ✅ Patent grant included
- ⚠️ Provide attribution
- ⚠️ State changes made

---

## 🙏 Acknowledgments

PARTH uses amazing open-source projects:

- **AI Models:** Meta (Llama), Mistral AI, Microsoft (Phi), DeepSeek, and many more
- **Frameworks:** LangChain, AutoGPT, MetaGPT, CrewAI
- **Voice:** OpenAI Whisper, Piper TTS, Chatterbox
- **Infrastructure:** Hugging Face Transformers, PyTorch, FastAPI

---

## 🌟 Star History

If you like PARTH, please ⭐ star this repository!

---

## 📞 Contact & Community

- **GitHub:** [Issues](https://github.com/[YOUR-USERNAME]/parth-ai/issues) | [Discussions](https://github.com/[YOUR-USERNAME]/parth-ai/discussions)
- **Discord:** [Join our community](#)
- **Twitter:** [@parth_ai](#)
- **Email:** your-email@example.com

---

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Core AI system
- ✅ Voice & chat interfaces
- ✅ Basic device control
- ✅ Multi-model orchestration

### Version 1.1 (Next)
- 🔄 iOS native app
- 🔄 Desktop apps (Electron/Tauri)
- 🔄 Enhanced vision capabilities
- 🔄 Plugin system

### Version 1.2
- 📅 Advanced automation
- 📅 Custom skill creation
- 📅 Community marketplace
- 📅 Multi-device sync

### Version 2.0 (Future)
- 🔮 AGI-level reasoning
- 🔮 Self-improvement
- 🔮 Robot control integration
- 🔮 Scientific research capabilities

---

<div align="center">

**Made with ❤️ by Prabhu and the open-source community**

**PARTH - Your Personal JARVIS is here! 🧠✨**

[⬆ Back to Top](#-parth---personal-advanced-reasoning--task-handling-intelligence)

</div>

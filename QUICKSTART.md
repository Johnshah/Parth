# 🚀 PARTH Quick Start Guide

## ⚡ Get Started in 5 Minutes

### For Android (Poco X6 Pro or any Android device)

1. **Install Termux** from F-Droid:
   ```
   https://f-droid.org/en/packages/com.termux/
   ```

2. **Open Termux** and paste these commands:
   ```bash
   pkg update -y && pkg upgrade -y
   pkg install -y git python termux-api
   git clone https://github.com/Johnshah/Parth.git parth-ai
   cd parth-ai
   pip install rich psutil pyyaml
   python parth.py
   ```

3. **Start chatting!**
   ```
   Prabhu: Hey Parth!
   Parth: Hello Prabhu! How can I help you today?
   ```

### For Desktop (Windows/Linux/macOS)

1. **Install Python 3.10+** from python.org

2. **Clone and run:**
   ```bash
   git clone https://github.com/Johnshah/Parth.git parth-ai
   cd parth-ai
   pip install rich psutil pyyaml
   python parth.py
   ```

## 🎯 What Can PARTH Do?

### Right Now (Basic Mode)
- ✅ Natural conversation
- ✅ Context awareness
- ✅ Memory of past conversations
- ✅ Task planning
- ✅ System information
- ✅ Command execution

### Coming Soon (Full Mode with AI Models)
- 🔄 Advanced reasoning (75+ AI models)
- 🔄 Voice interaction
- 🔄 Device control
- 🔄 Code generation
- 🔄 Image generation
- 🔄 Web automation

## 📝 Basic Commands

```bash
# Start PARTH
python parth.py

# With voice (when models are installed)
python parth.py --voice

# Web interface
python parth.py --mode web --port 8080

# Debug mode
python parth.py --debug

# Help
python parth.py --help
```

## 🧪 Test It Out

Try these:

```
Prabhu: Hello Parth
Prabhu: What can you do?
Prabhu: Tell me about this system
Prabhu: What's my name?
Prabhu: Help me with something
Prabhu: exit
```

## 📚 Next Steps

1. **Read the full docs:** [README.md](README.md)
2. **Install AI models:** [PARTH_SYSTEM_PROMPT.md](PARTH_SYSTEM_PROMPT.md)
3. **Android setup:** [docs/deployment/TERMUX_INSTALLATION.md](docs/deployment/TERMUX_INSTALLATION.md)
4. **Customize:** Edit `config/config.yaml`

## 🐛 Troubleshooting

**"Module not found":**
```bash
pip install rich psutil pyyaml
```

**"Permission denied":**
```bash
chmod +x parth.py
```

**Need help?**
- Check logs: `logs/parth.log`
- GitHub Issues: https://github.com/Johnshah/Parth/issues

## 🌟 Features Overview

| Feature | Status | Description |
|---------|--------|-------------|
| Chat Interface | ✅ Working | Terminal-based chat |
| Context Memory | ✅ Working | Remembers conversation |
| Task Planning | ✅ Working | Breaks down complex tasks |
| Configuration | ✅ Working | Customizable settings |
| Voice Input | 🔄 Coming | Whisper integration |
| Voice Output | 🔄 Coming | TTS integration |
| AI Models | 🔄 Coming | 75+ models |
| Device Control | 🔄 Coming | Full automation |
| Web Interface | 🔄 Coming | Browser-based UI |
| Mobile Apps | 🔄 Coming | Native Android/iOS |

## 💡 Pro Tips

1. **Use tab completion** in chat for faster typing
2. **Press Ctrl+C** to interrupt long responses
3. **Type 'exit'** to quit gracefully
4. **Check logs** for detailed information
5. **Customize personality** in config files

## 🎉 Welcome to PARTH!

You now have a basic AI assistant running. As you install more dependencies and models, PARTH will become more powerful!

**Repository:** https://github.com/Johnshah/Parth
**Your Assistant:** Parth
**Your Name:** Prabhu (customizable)

Enjoy! 🧠✨

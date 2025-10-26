# 📱 Complete Termux Installation Guide for PARTH AI

This is a **step-by-step guide** for installing PARTH on Android using Termux. Written for beginners - no technical knowledge needed!

## 🎯 What You'll Need

- **Android Phone:** Any Android device (optimized for Poco X6 Pro)
- **RAM:** At least 6GB (12GB recommended for best performance)
- **Storage:** At least 10GB free space
- **Internet:** For initial setup and downloads

---

## 📦 Step 1: Install Termux

### Method A: F-Droid (Recommended - Most Stable)

1. **Open your phone's browser** (Chrome, Firefox, etc.)
2. **Go to:** `https://f-droid.org`
3. **Tap "Download F-Droid"** button
4. **Install F-Droid** (you may need to enable "Install from Unknown Sources" in Settings)
5. **Open F-Droid** app
6. **Search for "Termux"**
7. **Install Termux** (tap Install button)
8. **Also install "Termux:API"** (important for device control!)

### Method B: GitHub (Alternative)

1. Open browser and go to: `https://github.com/termux/termux-app/releases`
2. Download the latest APK file (usually named `termux-app_vX.X.X+github-debug.apk`)
3. Install the APK
4. Also download and install `termux-api` from: `https://github.com/termux/termux-api/releases`

---

## 🚀 Step 2: Setup Termux

### 2.1: Open Termux

When you first open Termux, you'll see a **black screen with text** - this is normal! It's a terminal/command line.

### 2.2: Update Packages

**Copy and paste this command** (tap and hold in Termux to paste):

```bash
pkg update -y && pkg upgrade -y
```

**What this does:** Updates all software packages to latest versions  
**How long:** 2-5 minutes depending on internet speed  
**What you'll see:** Lots of text scrolling - this is normal!

### 2.3: Give Termux Storage Access

```bash
termux-setup-storage
```

**What happens:** A popup will appear asking for storage permission  
**What to do:** Tap "Allow" or "Grant"  
**Why:** This lets PARTH access your files, photos, etc.

### 2.4: Install Basic Tools

```bash
pkg install -y git python wget curl openssh termux-api
```

**What this installs:**
- `git` - Download code from GitHub
- `python` - Programming language PARTH runs on
- `wget` & `curl` - Download files
- `openssh` - Secure connections
- `termux-api` - Control Android device

**How long:** 5-10 minutes

---

## 💻 Step 3: Install PARTH AI

### 3.1: Download PARTH

```bash
cd ~
git clone https://github.com/[YOUR-GITHUB-USERNAME]/parth-ai.git
cd parth-ai
```

**What this does:**
- `cd ~` - Go to home directory
- `git clone` - Download PARTH from GitHub
- `cd parth-ai` - Enter PARTH folder

### 3.2: Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**How long:** 10-20 minutes (lots of packages to install)  
**What you'll see:** Progress bars and package names scrolling  
**Be patient!** This is downloading and installing many AI libraries

### 3.3: Install Node.js Dependencies (Optional - for web interface)

```bash
pkg install -y nodejs-lts
npm install
```

**How long:** 5-10 minutes

---

## 🧠 Step 4: Download AI Models

### 4.1: Automatic Model Setup

PARTH includes a setup script that automatically downloads the best models for your device:

```bash
python setup_models.py --device android --ram 12GB
```

**For different RAM:**
- 6-8GB RAM: `python setup_models.py --device android --ram 6GB`
- 12GB RAM: `python setup_models.py --device android --ram 12GB`
- 16GB+ RAM: `python setup_models.py --device android --ram 16GB`

**What this does:** Downloads optimized AI models for your device  
**How long:** 30-60 minutes (large downloads!)  
**Storage used:** 15-30GB depending on models

**💡 Tip:** Do this while connected to WiFi and charging!

### 4.2: What Models Get Downloaded

For **12GB RAM** (Poco X6 Pro), you'll get:

- **Reasoning:** Phi-3-mini (4bit quantized) - 2.3GB
- **Code Generation:** DeepSeek-Coder-6.7B (4bit) - 3.8GB  
- **Voice Recognition:** Whisper-medium - 1.5GB
- **Text-to-Speech:** Piper TTS - 50MB
- **Vision:** CLIP-ViT - 1.7GB
- **Embeddings:** BGE-large - 670MB

**Total:** ~10-15GB

---

## ✅ Step 5: Run PARTH for First Time

### 5.1: Basic Launch

```bash
python parth.py
```

**What you'll see:**
```
╔═══════════════════════════════════════════════╗
║              PARTH AI SYSTEM                  ║
║   Personal Advanced Reasoning & Task Handling ║
╚═══════════════════════════════════════════════╝

🚀 Initializing PARTH AI System...
📊 System: Linux aarch64 | RAM: 11.5GB | CPU: 8 cores
⚙️  Loading configuration from config/config.yaml
🧠 Initializing AI core...
✅ PARTH AI core initialized successfully
💬 Hello Prabhu! I'm Parth, your personal AI assistant...
```

### 5.2: Test PARTH

Type: `Hello Parth!`

PARTH should respond with a greeting!

### 5.3: Exit PARTH

Type: `exit` or press `Ctrl+D`

---

## 🎙️ Step 6: Enable Voice Features (Optional)

### 6.1: Install Audio Packages

```bash
pkg install -y pulseaudio
```

### 6.2: Run with Voice

```bash
python parth.py --voice
```

**What this does:** Enables voice recognition and speech  
**Wake word:** Say "Hey Parth" or "Parth" to activate  
**Note:** First-time voice model loading may take a few minutes

---

## 🚀 Step 7: Auto-Start PARTH on Boot (Optional)

### 7.1: Install Termux:Boot

Download and install **Termux:Boot** from F-Droid or GitHub

### 7.2: Create Startup Script

```bash
mkdir -p ~/.termux/boot
nano ~/.termux/boot/start-parth.sh
```

**In the editor, type:**

```bash
#!/data/data/com.termux/files/usr/bin/bash
cd ~/parth-ai
python parth.py --background --voice
```

**Save and exit:**
- Press `Ctrl+X`
- Press `Y`
- Press `Enter`

### 7.3: Make Script Executable

```bash
chmod +x ~/.termux/boot/start-parth.sh
```

**Now PARTH will start automatically** when your phone boots!

---

## 🌐 Step 8: Access Web Interface (Optional)

### 8.1: Start Web Server

```bash
python parth.py --mode web --port 8080
```

### 8.2: Open in Browser

On your phone, open browser and go to: `http://localhost:8080`

You'll see a web interface for PARTH!

### 8.3: Access from Other Devices

To access from PC/laptop on same WiFi:

1. Find your phone's IP address:
```bash
ifconfig
```
Look for `inet` address (usually starts with `192.168.`)

2. On PC/laptop browser, go to: `http://[YOUR-PHONE-IP]:8080`

---

## 🔧 Troubleshooting

### Problem: "Command not found"

**Solution:**
```bash
pkg install python
pkg install termux-api
```

### Problem: "Permission denied"

**Solution:**
```bash
termux-setup-storage
# Then allow permissions in popup
```

### Problem: "Out of memory"

**Solutions:**
1. Close other apps
2. Use smaller models:
```bash
python setup_models.py --device android --ram 6GB
python parth.py --model-size small
```

### Problem: Models downloading too slow

**Solution:**
- Use WiFi instead of mobile data
- Download during off-peak hours
- Pause and resume if needed (script resumes automatically)

### Problem: "Module not found" errors

**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

### Problem: Voice not working

**Solutions:**
1. Install audio packages:
```bash
pkg install -y pulseaudio
```

2. Grant microphone permission to Termux in Android Settings

3. Test microphone:
```bash
python test_audio.py
```

---

## 📊 Performance Tips for Poco X6 Pro

### Optimize for Best Performance

```bash
# Run in performance mode
python parth.py --performance-mode

# Use 4-bit quantization (less memory, still good quality)
python parth.py --quantization 4bit
```

### Battery Optimization

```bash
# Balanced mode (default)
python parth.py

# Battery saver mode
python parth.py --model-size small
```

### Check System Resources

```bash
# Check memory usage
free -h

# Check CPU usage
top

# Check storage
df -h
```

---

## 🎯 Quick Reference Commands

### Start PARTH
```bash
cd ~/parth-ai
python parth.py
```

### Start with Voice
```bash
python parth.py --voice
```

### Start Web Interface
```bash
python parth.py --mode web --port 8080
```

### Update PARTH
```bash
cd ~/parth-ai
git pull
pip install --upgrade -r requirements.txt
```

### Check Status
```bash
python parth.py --debug
```

### Stop PARTH
Press `Ctrl+C` or type `exit`

---

## 🌟 Next Steps

After installation:

1. **Customize:** Edit `config/config.yaml` for your preferences
2. **Learn Commands:** Read `docs/guides/COMMANDS.md`
3. **Explore Features:** Try different modes and capabilities
4. **Join Community:** Discord link in main README
5. **Contribute:** Report issues or add features!

---

## 🆘 Need Help?

- **Documentation:** Check `/docs` folder
- **GitHub Issues:** Report bugs or ask questions
- **Community:** Join our Discord server
- **Logs:** Check `logs/parth.log` for error details

---

**Congratulations! 🎉** PARTH is now installed and ready to use on your Poco X6 Pro!

Welcome to the future of personal AI assistance! 🧠✨

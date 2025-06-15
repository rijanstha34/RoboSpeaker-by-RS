# 🤖 RoboSpeaker by RS

RoboSpeaker is a simple Text-to-Speech desktop app built using Python's `gTTS`, `pygame`, and `tkinter`. It allows users to input any text and instantly hear it spoken aloud. This version is compiled into a standalone `.exe` file, so **no Python installation is needed** to run it.

---

## 📦 Features

- ✅ Convert text to speech using Google Text-to-Speech (gTTS)
- ✅ Clean and user-friendly GUI with `Tkinter`
- ✅ Real-time audio playback using `pygame`
- ✅ Auto-delete audio file after playback
- ✅ Works offline (after first internet use for gTTS)

---

## 📁 Files

- `RoboSpeaker.exe` – the standalone executable app (inside the `dist/` folder)
- `robospeaker_gui.py` – main Python source code
- `requirements.txt` – Python dependencies
- `.gitignore` – excludes unwanted files (e.g., `.mp3`, `.exe`, `__pycache__/`)
- `README.md` – this documentation

---

## 🚀 How to Run (Executable)

1. Go to the [`dist/`](./dist) folder.
2. Double-click the `RoboSpeaker.exe` file.
3. Type your text and click **Speak** to hear it aloud.
4. Click **Exit** to close the app.

---

## 🔧 For Developers

If you'd like to build or modify the source:

### 📥 Install Requirements

```bash
pip install -r requirements.txt

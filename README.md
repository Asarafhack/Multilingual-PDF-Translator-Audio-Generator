
<h1 align="center">🌐 Multilingual PDF Translator & Audio Generator</h1>

<p align="center">
  📄 ➜ 🌍 ➜ 🔊<br>
  <b>Upload a PDF → Translate it → Get it as Audio in Multiple Languages</b><br>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9-blue?logo=python" />
  <img src="https://img.shields.io/badge/pdf-translation-orange" />
  <img src="https://img.shields.io/badge/text--to--speech-tts-red" />
  <img src="https://img.shields.io/badge/languages-6+-brightgreen" />
  <img src="https://img.shields.io/github/license/Asarafhack/Multilingual-PDF-Translator-Audio-Generator" />
</p>

---

## 🧠 Project Overview

This project is a smart, AI-powered **PDF Translator and Text-to-Speech Generator** that allows users to:

- Upload PDF files with readable content
- Translate them into **6 languages**:
  > 🌐 English · 🐘 Tamil · 🕉️ Hindi · 🧵 Marathi · 🥖 French · 🌴 Malayalam
- Generate audio output (MP3 or playback)
- Use it for learning, accessibility, content reuse, or real-time assistance

---

## 🎯 Use Cases

✅ Visually Impaired Accessibility  
✅ Multilingual Education Tools  
✅ Government Documentation Support  
✅ Personal Productivity & Language Learning  
✅ Content Creators repurposing long PDFs into podcasts

---

## 🚀 Features

| Feature                  | Description                                                                  |
|--------------------------|------------------------------------------------------------------------------|
| 📤 PDF Upload            | Drag-and-drop or file-select interface                                       |
| 🌍 Multi-language Support| Built-in translation to Tamil, English, Hindi, Marathi, French, Malayalam   |
| 🔊 Audio Generation      | Uses TTS (like `gTTS` or `pyttsx3`) to create audio                          |
| 📄 Transcript Export     | Save translated text as `.txt` or `.docx`                                    |
| 🎧 Audio Download        | Download translated voice as `.mp3`                                          |
| 🖥️ GUI Option (Optional) | Can be implemented in Flask or Streamlit                                     |

---

## 🛠️ Tech Stack

```txt
🔹 Python 3.x
🔹 PyPDF2 / pdfplumber – PDF Text Extraction
🔹 googletrans – Translation API
🔹 gTTS / pyttsx3 – Text to Speech
🔹 Flask or Streamlit – Interface
🔹 FFMPEG – Optional audio enhancements



## 🛠️ Installation Guide (Windows & Linux)

Follow the instructions based on your operating system to install all dependencies and run the app.

---

### 🪟 For Windows Users

📌 Prerequisites:
- Python 3.9 or higher 👉 [Download here](https://www.python.org/downloads/windows/)
- Git CLI 👉 [Git for Windows](https://git-scm.com/download/win)
- Internet connection for Google Translate API

📥 Installation Command:

```bash
git clone https://github.com/Asarafhack/Multilingual-PDF-Translator-Audio-Generator.git
cd Multilingual-PDF-Translator-Audio-Generator
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt


python app.py        # For CLI version
streamlit run app.py # For Web version


🐧 For Linux / Ubuntu Users
📌 Prerequisites:

Python 3.x (sudo apt install python3 python3-pip)

Git (sudo apt install git)

FFMPEG for audio playback (sudo apt install ffmpeg)

📥 Installation Command:

bash
Copy
Edit
git clone https://github.com/Asarafhack/Multilingual-PDF-Translator-Audio-Generator.git
cd Multilingual-PDF-Translator-Audio-Generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
▶️ To Run:

bash
Copy
Edit
python3 app.py           # For CLI version
streamlit run app.py     # For Web version
🧪 Required Python Libraries
These are installed automatically from requirements.txt, but here’s what you’re getting:

txt
Copy
Edit
PyPDF2
googletrans==4.0.0rc1
gTTS
pyttsx3
streamlit
pdfplumber
ffmpeg-python
🛡️ Optional (for enhancement):

deep-translator

pydub (for advanced audio editing)

SpeechRecognition (if adding voice input)

✅ Pro Tip:
If anything fails during TTS on Windows, run:

bash
Copy
Edit
pip install pyttsx3 pypiwin32

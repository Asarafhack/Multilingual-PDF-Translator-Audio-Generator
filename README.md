# Multilingual-PDF-Translator-Audio-Generator

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

import os
import fitz  # PyMuPDF for PDF text extraction
from flask import Flask, render_template, request, send_from_directory, jsonify, url_for
from gtts import gTTS
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
from deep_translator import GoogleTranslator
import uuid

# Download required NLTK data
nltk.download("punkt")

# Initialize Flask app
app = Flask(__name__)

# Define folders
UPLOAD_FOLDER = "uploads/"
OUTPUT_FOLDER = "output/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def extract_text(pdf_path):
    """Extracts text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join(page.get_text("text") for page in doc)
        return text.strip() if text else "No text found in PDF."
    except Exception as e:
        return f"Error extracting text: {str(e)}"


def summarize_text(text, sentence_count=5):
    """Summarizes text using LSA algorithm."""
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentence_count)
        return " ".join(str(sentence) for sentence in summary)
    except Exception as e:
        return f"Error summarizing text: {str(e)}"


def translate_text(text, target_lang):
    """Translates text into the selected language using Deep Translator."""
    try:
        translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Error translating text: {str(e)}"


def text_to_speech(text, lang, output_path):
    """Converts text to speech and saves as an MP3 file."""
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        return output_path
    except Exception as e:
        return f"Error in TTS conversion: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_pdf():
    try:
        file = request.files.get("pdf")
        target_lang = request.form.get("language")

        if not file or not target_lang:
            return jsonify({"error": "Missing file or language"}), 400

        unique_id = str(uuid.uuid4())
        pdf_filename = f"{unique_id}.pdf"
        pdf_path = os.path.join(UPLOAD_FOLDER, pdf_filename)
        file.save(pdf_path)

        print(f"Saved PDF: {pdf_path}")

        # Extract text
        extracted_text = extract_text(pdf_path)
        print(f"Extracted Text: {extracted_text[:500]}")  # Print only first 500 chars

        # Summarize
        summarized_text = summarize_text(extracted_text)
        print(f"Summarized Text: {summarized_text}")

        # Translate
        translated_text = translate_text(summarized_text, target_lang)
        print(f"Translated Text: {translated_text}")

        # Convert to Speech
        audio_filename = f"translated_audio_{unique_id}.mp3"
        audio_path = os.path.join(OUTPUT_FOLDER, audio_filename)
        result = text_to_speech(translated_text, target_lang, audio_path)

        if "Error" in result:
            return jsonify({"error": result}), 500

        return jsonify({
            "audio_url": url_for("download_file", filename=audio_filename, _external=True),
            "open_audio_url": url_for("open_audio", filename=audio_filename, _external=True)
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/output/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)


@app.route('/play/<filename>')
def open_audio(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)

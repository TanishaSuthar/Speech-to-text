import whisper
import gradio as gr
import os
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from pydub import AudioSegment

# Load a stronger Whisper model for better accuracy (you can also try "medium" or "large")
model = whisper.load_model("medium")

def transcribe_audio(audio_path, language):
    if audio_path is None:
        return "Please upload or record an audio file."

    try:
        # Convert audio to 16kHz mono WAV for consistency
        audio = AudioSegment.from_file(audio_path)
        audio = audio.set_channels(1).set_frame_rate(16000)
        processed_path = "converted.wav"
        audio.export(processed_path, format="wav")

        # Run Whisper transcription in native language (not translation)
        result = model.transcribe(processed_path, language=language, task="transcribe")
        transcribed_text = result["text"]
        detected_lang = result.get("language", "unknown")

        # Optional: Convert ITRANS-style Hindi to Devanagari if needed
        if language == "hi":
            # Transliterate only if text seems Romanized
            if any(char in "abcdefghijklmnopqrstuvwxyz" for char in transcribed_text.lower()):
                transcribed_text = transliterate(transcribed_text, sanscript.ITRANS, sanscript.DEVANAGARI)

        return f"🗣 Detected: {detected_lang.upper()}\n\n📝 Text: {transcribed_text}"

    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio Interface
interface = gr.Interface(
    fn=transcribe_audio,
    inputs=[
        gr.Audio(type="filepath", label="🎙 Upload or Record Audio"),
        gr.Dropdown(choices=["en", "hi"], value="hi", label="🌐 Select Language")
    ],
    outputs="text",
    title="🎤 Whisper Speech-to-Text (English + Hindi Devanagari)",
    description="Accurate transcription of English and Hindi audio. Hindi output is shown in देवनागरी script.",
)

# Correct main check
if __name__ == "__main__":
    interface.launch()

#  Whisper Speech-to-Text (English + Hindi Devanagari)

This project uses OpenAI's Whisper model to transcribe speech audio in **English** and **Hindi**, with Hindi transcriptions outputted in **Devanagari** script instead of Roman or Urdu.

##  Features

- Transcribes audio recordings or uploads in English and Hindi
- Converts Romanized Hindi text to proper **देवनागरी** using `indic-transliteration`
- Gradio interface for ease of use
- Automatic conversion to 16kHz mono WAV for better Whisper performance
- Language selector (English / Hindi)

---

##  Technologies Used

| Technology              | Purpose                              |
|-------------------------|--------------------------------------|
| `openai-whisper`        | Speech-to-text model                 |
| `gradio`                | Web-based user interface             |
| `pydub`                 | Audio format conversion              |
| `indic-transliteration` | Romanized Hindi → Devanagari script  |
| `ffmpeg` (system tool)  | Required backend for audio processing|

---

##  Project sturcture
whisper-devanagari-transcription/
- stt_app.py                    # Main application code (Gradio UI + transcription)
- requirements.txt           # Python dependencies
- README.md                  # Project documentation

---


## ⚙ Setup and Installation

###  Prerequisites

- Python 3.8 or higher
- [FFmpeg](https://ffmpeg.org/download.html)
- Git (optional, for cloning)

---

###  Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone [https://github.com/yourusername/whisper-devanagari-transcription.git](https://github.com/TanishaSuthar/Speech-to-text/tree/main)
cd speech-to-text
```

> Or download the ZIP manually and extract it.

#### 2. Install Requirements

```bash
pip install -r requirements.txt
```

#### 3. Install FFmpeg

FFmpeg is required by Whisper and Pydub.

- **Windows**:  
  Download from [FFmpeg Downloads](https://ffmpeg.org/download.html) and add to `PATH`.
---

#### 4. Run the App

```bash
python stt_app.py
```

Your browser will open with the Gradio interface. Select language (`hi` or `en`), upload or record audio, and view results.

---

##  Example Output

- **English Audio**:  
  _"Hello, how are you?"_  
  → `Hello, how are you?`

- **Hindi Audio**:  
  _"यह एक सुंदर कहानी है।"_  
  → `यह एक सुंदर कहानी है।`

---

##  Dependencies

See [`requirements.txt`](./requirements.txt):

```txt
openai-whisper
gradio
pydub
indic-transliteration
```

---

##  Model Used

- [`medium`](https://github.com/openai/whisper) Whisper model for better accuracy.

You can change to `"base"`, `"small"`, or `"large"` in `stt_app.py` if desired.


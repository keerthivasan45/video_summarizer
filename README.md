# 🎥 AI Video Summarizer from YouTube

This project takes a YouTube URL, downloads the video, extracts audio, transcribes it using OpenAI's Whisper, and summarizes it using the Pegasus transformer model.

---

## 🚀 Features

- 🔗 Accepts YouTube video URLs
- 🎵 Extracts audio using `yt_dlp` and `moviepy`
- 🧠 Transcribes using OpenAI's `whisper`
- 📝 Summarizes using `Pegasus` transformer model
- 📄 Saves both the transcript and the summary

---

## 📦 Tech Stack

- Python 3.10+
- `yt_dlp` – for downloading YouTube videos
- `moviepy` – for audio processing
- `whisper` – for transcription
- `transformers` (`Pegasus`) – for summarization
- `torch` – backend for models

---

## 📁 Folder Structure

video_summarizer/
│
├── app.py # Optional: Streamlit UI
├── summarizer.py # Main logic (YouTube > Audio > Transcript > Summary)
├── transcript.txt # Generated transcript
├── summary.txt # Final summary
├── temp_audio.webm # Temporary audio file from YouTube
├── audio.wav # Converted audio for Whisper
├── samplevideo.mp4 # (Optional test file)
├── .gitignore
├── .gitattributes
└── templates/ # (If using UI)



---

## 🔧 Setup Instructions
1. Clone the repository
2. Create & activate a virtual environment
3.Install dependencies
  pip install -r requirements.txt
  Make sure ffmpeg is installed and accessible from your PATH.
4.Run the Python script
  streamlit run main.py

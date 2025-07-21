import yt_dlp
import whisper
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os


def download_audio_from_youtube(url, output_path="audio.wav"):
    print("🎥 Downloading and extracting audio from YouTube...")

    # Clean up old files if they exist
    if os.path.exists("temp_audio.wav"):
        os.remove("temp_audio.wav")
    if os.path.exists(output_path):
        os.remove(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Try renaming downloaded file to consistent name
    for ext in ['wav', 'mp3', 'm4a']:
        try:
            os.rename(f"temp_audio.{ext}", output_path)
            break
        except FileNotFoundError:
            continue

    return output_path


def transcribe_audio(audio_path):
    print("🗣️ Transcribing audio using Whisper (base model)...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, task="translate")  # Use translate to always get English

    transcript_text = result['text']
    
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript_text)

    return transcript_text

def summarize_text(text):
    print("🧠 Summarizing with Pegasus model...")
    tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-xsum")

    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=100, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    return summary

# === MAIN PIPELINE ===
if __name__ == '__main__':
    video_url = input("📥 Enter YouTube video URL: ").strip()
    
    # Step 1: Download audio from YouTube
    audio = download_audio_from_youtube(video_url)

    # Step 2: Transcribe audio
    transcript = transcribe_audio(audio)
    print("\n📜 Transcript:\n")
    print(transcript)

    # Step 3: Summarize text
    summary = summarize_text(transcript)
    print("\n✅ Summary:\n")
    print(summary)

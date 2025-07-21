from flask import Flask, render_template, request
import os
from summarizer import download_audio_from_youtube, transcribe_audio, summarize_text

app = Flask(__name__)
OUTPUT_DIR = 'outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript, summary = '', ''
    
    if request.method == 'POST':
        url = request.form.get('video_url')
        if url:
            try:
                print("🎯 Received URL")
                
                # Download audio
                print("📥 Downloading audio...")
                audio_path = os.path.join(OUTPUT_DIR, 'audio.wav')
                download_audio_from_youtube(url, output_path=audio_path)
                print("✅ Downloaded audio")

                # Transcribe
                print("📝 Transcribing...")
                transcript = transcribe_audio(audio_path)
                print("✅ Transcription complete")

                # Summarize
                print("🧠 Summarizing...")
                summary = summarize_text(transcript)
                print("✅ Summary ready")

            except Exception as e:
                print("❌ Error:", e)
                transcript = f"⚠️ Error: {str(e)}"
                summary = "❌ Could not generate summary due to error."

    return render_template('index.html', transcript=transcript, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)

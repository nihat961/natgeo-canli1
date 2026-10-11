import subprocess
import shutil
from flask import Flask, redirect

app = Flask(__name__)

# National Geographic Animals Canlı Yayın Kimliği
VIDEO_ID = "MiQe9ob9aDc"

@app.route("/natgeo.m3u8")
def get_live_stream():
    try:
        ytdlp_path = shutil.which("yt-dlp") or "yt-dlp"
        
        # YouTube bot engelini kıran tarayıcı taklidi (User-Agent) komuta eklendi
        komut = [
            ytdlp_path, 
            "--get-url", 
            "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            f"https://youtube.com{VIDEO_ID}"
        ]
        
        guncel_link = subprocess.check_output(komut).decode("utf-8").strip()
        return redirect(guncel_link)
    except Exception as e:
        return f"Hata: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

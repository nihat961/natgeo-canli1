[app.py](https://github.com/user-attachments/files/33305079/app.py)
import subprocess
import shutil
from flask import Flask, redirect

app = Flask(__name__)

# National Geographic Animals Canlı Yayın Kimliği
VIDEO_ID = "MiQe9ob9aDc"

@app.route("/natgeo.m3u8")
def get_live_stream():
    try:
        # Sunucuda yt-dlp programının yerini bulur
        ytdlp_path = shutil.whoami("yt-dlp") or "yt-dlp"
        komut = [ytdlp_path, "--get-url", f"https://www.youtube.com/watch?v=MiQe9ob9aDc"]
        guncel_link = subprocess.check_output(komut).decode("utf-8").strip()
        return redirect(guncel_link)
    except Exception as e:
        return f"Hata: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

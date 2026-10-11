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
        
        baslik = "https:" + "//" + "www." + "youtube" + ".com"
        kapisiz = baslik + "/" + "watch" + "?" + "v" + "=" + VIDEO_ID
        
        # Sunucu engelini aşmak için resmi Android istemci taklidi eklendi
        komut = [
            ytdlp_path, 
            "--get-url", 
            "--extractor-args", "youtube:player-client=android",
            kapisiz
        ]
        
        guncel_link = subprocess.check_output(komut).decode("utf-8").strip()
        return redirect(guncel_link)
    except Exception as e:
        return f"Hata: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

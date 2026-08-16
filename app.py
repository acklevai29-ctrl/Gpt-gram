from flask import Flask
import threading
import os
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def health():
    return "Bot is running!", 200

if __name__ == "__main__":
    # Start bot in background
    def run_bot():
        subprocess.run([sys.executable, "bot.py"])
    
    threading.Thread(target=run_bot, daemon=True).start()
    
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

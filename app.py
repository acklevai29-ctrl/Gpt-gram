from flask import Flask
import threading
import os
import logging
import subprocess
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running!", 200

def run_bot():
    """Run the bot.py file"""
    try:
        # Run the original bot.py from the repo
        subprocess.run([sys.executable, "bot.py"])
    except Exception as e:
        logger.error(f"Bot crashed: {e}")

if __name__ == "__main__":
    # Start bot in background
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    logger.info("Bot started")
    
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

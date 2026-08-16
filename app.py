from flask import Flask, request
import os
import logging
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Import bot functions
from bot import main as start_bot

@app.route('/')
def health():
    return "✅ Bot is running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle webhook updates"""
    from telegram import Update
    from bot import application
    
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.process_update(update)
    return "OK", 200

if __name__ == "__main__":
    # Start bot in background
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

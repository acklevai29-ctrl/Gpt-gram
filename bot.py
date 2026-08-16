import os
import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *AI Assistant Bot*\n\n"
        "Send me a message and I'll respond!\n"
        "Commands:\n"
        "/start - Show this message\n"
        "/ping - Check if bot is alive",
        parse_mode='Markdown'
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Bot is alive!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    logger.info(f"Received: {user_msg}")
    
    # Simple echo with AI-like responses
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! Nice to meet you!",
        "how are you": "I'm doing great, thanks for asking!",
        "help": "I'm here to assist you! Ask me anything.",
        "bye": "Goodbye! Have a great day!",
    }
    
    # Check for keywords in message
    msg_lower = user_msg.lower()
    response = None
    
    for key, value in responses.items():
        if key in msg_lower:
            response = value
            break
    
    if response:
        await update.message.reply_text(response)
    else:
        # Default response
        await update.message.reply_text(
            f"🤔 I received: '{user_msg}'\n\n"
            f"I'm a simple bot right now. Try saying 'hi', 'hello', or 'help'!"
        )

def main():
    logger.info("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("Bot is polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

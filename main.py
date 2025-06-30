import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start, info, trivia, settings, admin
from flask import Flask
import threading
import os

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Flask app for Koyeb healthcheck
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

def main():
    from handlers import register_handlers
    TOKEN = os.getenv("BOT_TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    register_handlers(application)
    threading.Thread(target=run_flask).start()
    application.run_polling()

if __name__ == '__main__':
    main()

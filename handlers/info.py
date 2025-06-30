from telegram.ext import MessageHandler, filters
from utils.fetcher import fetch_movie_info
from utils.textcleaner import correct_spelling

async def movie_info(update, context):
    query = update.message.text
    corrected = correct_spelling(query)
    if corrected != query:
        await update.message.reply_text(f"🔍 Aapka matlab: *{corrected}* tha?", parse_mode='Markdown')

    info = fetch_movie_info(corrected)
    if info:
        await update.message.reply_text(info, disable_web_page_preview=True)
    else:
        await update.message.reply_text("😢 Koi info nahi mili. Film ka naam sahi likhein.")

info_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, movie_info)

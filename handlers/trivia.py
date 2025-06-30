from telegram.ext import CommandHandler
from database.mongo import get_random_trivia

async def trivia(update, context):
    q = get_random_trivia()
    await update.message.reply_text(f"🎬 *Trivia Time!*\n\n{q['question']}", parse_mode='Markdown')

trivia_handler = CommandHandler("trivia", trivia)

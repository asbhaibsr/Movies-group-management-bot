from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("➕ Mujhe Group Mein Jodein", url=f"https://t.me/{context.bot.username}?startgroup=true")],
        [InlineKeyboardButton("❓ Madad", callback_data="help")],
        [InlineKeyboardButton("🎬 Official Movie Group", url="https://t.me/istreamX")],
        [InlineKeyboardButton("📣 Promotion", url="https://t.me/asbhaibsr")],
    ]
    await update.message.reply_text(
        "👋 Namaste! Main ek movie info & trivia bot hoon.\n"
        "Mujhse film, web series aur anime ke baare mein puchhiye, aur khelte rahiye film trivia!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

start_cmd = CommandHandler("start", start)

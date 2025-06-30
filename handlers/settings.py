from telegram.ext import CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from database.mongo import get_group_settings, toggle_feature

async def settings(update, context):
    if not update.message.chat.type == "private":
        await update.message.reply_text("Ye command sirf private chat mein use karein.")
        return

    chat_id = int(context.args[0]) if context.args else None
    if not chat_id:
        await update.message.reply_text("Chat ID nahi mila.")
        return

    settings = get_group_settings(chat_id)
    buttons = [
        [InlineKeyboardButton(f"🎬 Movie Info: {'ON' if settings['movie_info'] else 'OFF'}", callback_data=f"toggle_movie_{chat_id}")],
        [InlineKeyboardButton(f"🧠 Trivia: {'ON' if settings['trivia'] else 'OFF'}", callback_data=f"toggle_trivia_{chat_id}")],
    ]
    await update.message.reply_text("Group Settings:", reply_markup=InlineKeyboardMarkup(buttons))

settings_handler = CommandHandler("settings", settings)

from telegram.ext import CommandHandler
from database.mongo import broadcast_all

async def broadcast(update, context):
    if str(update.effective_user.id) != str(context.bot_data.get("OWNER_ID")):
        return
    text = " ".join(context.args)
    count = broadcast_all(text)
    await update.message.reply_text(f"📣 Broadcasted to {count} chats.")

admin_handler = CommandHandler("broadcast", broadcast)

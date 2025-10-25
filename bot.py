import time
import logging
from telegram.ext import Updater, MessageHandler, Filters

# 🔹 Setup logging
logging.basicConfig(
    filename="bot.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 🔹 Hardcoded token (using your provided fake one as if real)
TOKEN = "8384276664:AAGrbyavd2lE5_aEGpudfExghrvIH1g49OU"

def mono_values(update, context):
    lines = update.message.text.splitlines()
    formatted = []
    for line in lines:
        if ":" in line:
            label, val = line.split(":", 1)
            val = val.strip()
            formatted.append(f"{label.strip()}: `{val}`")
        else:
            formatted.append(line)
    update.message.reply_text("\n".join(formatted), parse_mode="MarkdownV2")

while True:
    try:
        print("🚀 Bot is starting...")
        updater = Updater(TOKEN)
        dp = updater.dispatcher
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, mono_values))

        updater.start_polling()
        updater.idle()
    except Exception as e:
        print("⚠️ Bot crashed:", e)
        logging.error("Bot crashed", exc_info=True)
        print("🔄 Restarting in 5 seconds...")
        time.sleep(5)

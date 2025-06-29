from telegram.ext import Updater, CommandHandler
import logging

BOT_TOKEN = "7872889474:AAFC7pARBWCDWjXCLLHEja8tCpcHnQxDA2c"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

def start(update, context):
    update.message.reply_text("Бот работает!")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

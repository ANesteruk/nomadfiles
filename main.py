import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started!")

def start_command(update, context):
    update.message.reply_text('Type something to start')

def handle_message(update, context):
    text=str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling(0)
    updater.idle()

main()
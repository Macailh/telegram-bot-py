from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher

TOKEN = "OKEN"


def route(update, context):
    text = update.message.text

    # Control what your chatbot replies in this block of code!

    update.message.reply_text(text)


updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, route))
updater.start_polling()

print("Your telegram bot is running!")

updater.idle()

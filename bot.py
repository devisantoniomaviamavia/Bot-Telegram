from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Olá! Bot funcionando.")

updater = Updater("7999705337:AAHSVp2GmGxitTXGogm_7cwwTzr5tX51NHE", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()

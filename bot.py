from telegram.ext import Updater, CommandHandler
from flask import Flask

app = Flask(__name__)

def start(update, context):
    update.message.reply_text("Olá! Bot funcionando.")

updater = Updater("7999705337:AAHSVp2GmGxitTXGogm_7cwwTzr5tX51NHE", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

@app.route('/')
def home():
    return "Bot está online"

if __name__ == '__main__':
    updater.start_polling()
    app.run(host='0.0.0.0', port=5000)

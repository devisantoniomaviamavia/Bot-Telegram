saldo = user_balances.get(user_id, 0)
    update.message.reply_text(f"💰 Seu saldo: R{saldo:.2f}")

def sacar(update: Update, context: CallbackContext):
    update.message.reply_text("Para sacar, envie uma mensagem ao admin com seu número M-Pesa: +258857595392")

def ajuda(update: Update, context: CallbackContext):
    update.message.reply_text("📌 Use os botões para ver anúncios, verificar saldo ou sacar.\nVocê ganha R$0,25 por anúncio assistido.")

Flask route para manter vivo
@app.route('/')
def home():
    return "Bot online"

if _name_ == '_main_':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ver_anuncio", ver_anuncio))
    dp.add_handler(CommandHandler("saldo", saldo))
    dp.add_handler(CommandHandler("sacar", sacar))
    dp.add_handler(CommandHandler("ajuda", ajuda))

    updater.start_polling()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

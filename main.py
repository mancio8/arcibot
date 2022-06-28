import time

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "5546900846:AAFLj45vtz1WKXFM_KdO-lNklgoGoxQkRPs"
def start(update, context):
    update.message.reply_photo(open("logo.jpeg", 'rb'))

calcio_B="Regole Calcio balilla umano"
biliardino= "Regole Biliardino"
fifa= "Regole FIFA 22"
freccette= "Regole Frecette"
pingpong= "Regole Ping Pong"

'''''
def regole(update, context):

    update.message.reply_text("Calcio Balilla Umano")
    update.message.reply_photo(open("REGOLAMENTO CALCIO BALILLA UMANO.jpg", 'rb'))
    update.message.reply_text("Fifa 22")
    update.message.reply_photo(open("regolamento fifa 22.jpg", 'rb'))
    update.message.reply_text("Freccette")
    update.message.reply_photo(open("regolamento freccette.jpg", 'rb'))
    update.message.reply_text("Ping Pong")
    update.message.reply_photo(open("regolamento ping pong.jpg", 'rb'))
    update.message.reply_text("Biliardino")
    update.message.reply_photo(open("regolamento BILIARDINO.jpg", 'rb'))
'''
def regole(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(calcio_B)], [KeyboardButton("Regole FIFA 22")], [KeyboardButton("Regole Frecette")], [KeyboardButton("Regole Ping Pong")], [KeyboardButton("Regole Biliardino")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scegli il regolamento che vuoi leggere",
    reply_markup=ReplyKeyboardMarkup(buttons))



def invio(update: Update, context: CallbackContext):
    if calcio_B in update.message.text:
        update.message.reply_photo(open("REGOLAMENTO CALCIO BALILLA UMANO.jpg", 'rb'))
    if fifa in update.message.text:
        update.message.reply_photo(open("regolamento fifa 22.jpg", 'rb'))
    if pingpong in update.message.text:
        update.message.reply_photo(open("regolamento ping pong.jpg", 'rb'))
    if freccette in update.message.text:
        update.message.reply_photo(open("regolamento freccette.jpg", 'rb'))
    if biliardino in update.message.text:
        update.message.reply_photo(open("regolamento BILIARDINO.jpg", 'rb'))


def squadre(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("Squadre calcio balilla umano")], [KeyboardButton("Giocatori FIFA 22")], [KeyboardButton("Giocatori Frecette")], [KeyboardButton("Giocatori Ping Pong")], [KeyboardButton("Squadre Biliardino")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scegli le squadre che vuoi vedere",
    reply_markup=ReplyKeyboardMarkup(buttons))
def gironi(update, context):
    update.message.reply_text("Gironi del calcio balilla umano")
def partite(update, context):
    update.message.reply_text("Partite del calcio Balilla umano")



updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('regole', regole))
updater.dispatcher.add_handler(CommandHandler('squadre', squadre))
updater.dispatcher.add_handler(CommandHandler('gironi', gironi))
updater.dispatcher.add_handler(CommandHandler('partite', partite))
updater.dispatcher.add_handler(MessageHandler(Filters.text, invio))
updater.start_polling()
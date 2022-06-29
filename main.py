import time

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "5546900846:AAFLj45vtz1WKXFM_KdO-lNklgoGoxQkRPs"
def start(update, context):
    update.message.reply_photo(open("Locandina.jpeg", 'rb'))

calcio_B="Regole Calcio balilla umano"
biliardino= "Regole Biliardino"
fifa= "Regole FIFA 22"
freccette= "Regole Freccette"
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
    buttons = [[KeyboardButton(calcio_B)], [KeyboardButton("Regole FIFA 22")], [KeyboardButton("Regole Freccette")], [KeyboardButton("Regole Ping Pong")], [KeyboardButton("Regole Biliardino")]]
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
    if "Gironi calcio balilla umano" in update.message.text:
        update.message.reply_text("Presto disponibili")
        #update.message.reply_photo(open("GironeA.jpg", 'rb'))
        #update.message.reply_photo(open("GironeB.jpg", 'rb'))
        #update.message.reply_photo(open("GironeC.jpg", 'rb'))
        #update.message.reply_photo(open("GironeD.jpg", 'rb'))
    if "Gironi FIFA 22" in update.message.text:
        update.message.reply_text("Presto disponibili")
        #update.message.reply_photo(open("FifaA.jpg", 'rb'))
        #update.message.reply_photo(open("FifaB.jpg", 'rb'))
        #update.message.reply_photo(open("FifaC.jpg", 'rb'))
        #update.message.reply_photo(open("FifaD.jpg", 'rb'))
    if "Gironi Ping Pong" in update.message.text:
        update.message.reply_text("Presto disponibili")
        #update.message.reply_photo(open("PingA.jpg", 'rb'))
        #update.message.reply_photo(open("PingB.jpg", 'rb'))
        #update.message.reply_photo(open("PingC.jpg", 'rb'))
        #update.message.reply_photo(open("PingD.jpg", 'rb'))
    if "Gironi Biliardino" in update.message.text:
        update.message.reply_text("Presto disponibili")
        #update.message.reply_photo(open("BilA.jpg", 'rb'))
        #update.message.reply_photo(open("BilB.jpg", 'rb'))
        #update.message.reply_photo(open("BilC.jpg", 'rb'))
        #update.message.reply_photo(open("BilD.jpg", 'rb'))
    if "Squadre Biliardino" in update.message.text:
        update.message.reply_text("Presto disponibili")
    if "Squadre calcio balilla umano" in update.message.text:
        update.message.reply_text("Presto disponibili")
    if "Giocatori FIFA 22" in update.message.text:
        update.message.reply_text("Presto disponibili")
    if "Giocatori Freccette" in update.message.text:
        update.message.reply_text("Presto disponibili")
    if "Giocatori Ping Pong" in update.message.text:
        update.message.reply_text("Presto disponibili")
    if "Partite di stasera" in update.message.text:
        update.message.reply_text("Presto disponibili")
    if "Risultati partite" in update.message.text:
        update.message.reply_text("Presto disponibili")
    if "Prossime partite" in update.message.text:
        update.message.reply_text("Presto disponibili")
    if "Classifiche calcio balilla umano" in update.message.text:
        update.message.reply_text("Presto disponibili")
        #update.message.reply_photo(open("GironeA.jpg", 'rb'))
        #update.message.reply_photo(open("GironeB.jpg", 'rb'))
        #update.message.reply_photo(open("GironeC.jpg", 'rb'))
        #update.message.reply_photo(open("GironeD.jpg", 'rb'))
    if "Classifiche FIFA 22" in update.message.text:
        update.message.reply_text("Presto disponibili")
        #update.message.reply_photo(open("FifaA.jpg", 'rb'))
        #update.message.reply_photo(open("FifaB.jpg", 'rb'))
        #update.message.reply_photo(open("FifaC.jpg", 'rb'))
        #update.message.reply_photo(open("FifaD.jpg", 'rb'))
    if "Classifiche Ping Pong" in update.message.text:
        update.message.reply_text("Presto disponibili")
        #update.message.reply_photo(open("PingA.jpg", 'rb'))
        #update.message.reply_photo(open("PingB.jpg", 'rb'))
        #update.message.reply_photo(open("PingC.jpg", 'rb'))
        #update.message.reply_photo(open("PingD.jpg", 'rb'))
    if "Classifiche Biliardino" in update.message.text:
        update.message.reply_text("Presto disponibili")
        #update.message.reply_photo(open("BilA.jpg", 'rb'))
        #update.message.reply_photo(open("BilB.jpg", 'rb'))
        #update.message.reply_photo(open("BilC.jpg", 'rb'))
        #update.message.reply_photo(open("BilD.jpg", 'rb'))



def squadre(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("Squadre calcio balilla umano")], [KeyboardButton("Giocatori FIFA 22")], [KeyboardButton("Giocatori Freccette")], [KeyboardButton("Giocatori Ping Pong")], [KeyboardButton("Squadre Biliardino")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scegli le squadre che vuoi vedere",
    reply_markup=ReplyKeyboardMarkup(buttons))

def gironi(update, context):
    buttons = [[KeyboardButton("Gironi calcio balilla umano")], [KeyboardButton("Gironi FIFA 22")],
               [KeyboardButton("Gironi Ping Pong")], [KeyboardButton("Gironi Biliardino")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scegli il torneo di cui vuoi vedere i gironi: ",
                             reply_markup=ReplyKeyboardMarkup(buttons))
def partite(update, context):
    buttons = [[KeyboardButton("Partite di stasera")], [KeyboardButton("Risultati partite")],
               [KeyboardButton("Prossime partite")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scegli le partite che ti interessano: ",
                             reply_markup=ReplyKeyboardMarkup(buttons))

def classifiche(update, context):
    buttons = [[KeyboardButton("Classifiche calcio balilla umano")], [KeyboardButton("Classifiche FIFA 22")],
               [KeyboardButton("Classifiche Ping Pong")], [KeyboardButton("Classifiche Biliardino")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scegli la classifica che vuoi visualizzare: ",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def premi(update, context):
    update.message.reply_photo(open("PremiCB.jpg", 'rb'))
    update.message.reply_photo(open("PremiFr.jpg", 'rb'))
    update.message.reply_photo(open("PremioB.jpg", 'rb'))
    update.message.reply_photo(open("PremioPP.jpg", 'rb'))
    update.message.reply_photo(open("PremioF.jpg", 'rb'))


updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('regole', regole))
updater.dispatcher.add_handler(CommandHandler('squadre', squadre))
updater.dispatcher.add_handler(CommandHandler('gironi', gironi))
updater.dispatcher.add_handler(CommandHandler('partite', partite))
updater.dispatcher.add_handler(CommandHandler('classifiche', classifiche))
updater.dispatcher.add_handler(CommandHandler('premi', premi))
updater.dispatcher.add_handler(MessageHandler(Filters.text, invio))
updater.start_polling()
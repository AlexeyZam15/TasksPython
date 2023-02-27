from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE, send: str):
    send = send.replace("\n", "\\n")
    file = open('db.csv', 'a', encoding='utf-8')
    file.write(f'{datetime.datetime.now().time().strftime("%H:%M")}, {update.effective_user.id},'
               f' {update.effective_user.first_name}, {update.effective_user.last_name},'
               f' {update.message.text}, "{send}"\n')

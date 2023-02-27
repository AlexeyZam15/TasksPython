from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import log


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    send = f'Ну привет, {update.effective_user.first_name}'
    await update.message.reply_text(send)
    await log(update, context, send)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    send = '/hi\n/time\n/sum'
    await update.message.reply_text(send)
    await log(update, context, send)


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    send = f'{datetime.datetime.now().time().strftime("%H:%M")}'
    await update.message.reply_text(send)
    await log(update, context, send)


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()  # /sum 123 456
    try:
        total = int(items[len(items) - 1])
        send = ''
        for i in range(1, len(items) - 1):
            total += int(items[i])
            send += f'{items[i]} + '
        send += f'{items[len(items) - 1]} = {total}'
    except ValueError:
        send = 'Неправильный тип данных'
    await update.message.reply_text(send)
    await log(update, context, send)

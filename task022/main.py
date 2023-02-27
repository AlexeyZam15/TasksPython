from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

# Создание простого телеграм бота
# 1. Установить python пакет для работы с телеграм ботом
# 2. Получить токен от BotFather
# 3. Сделать несколько простых команд для бота
# 4. Дополнить функционалом ведения лог-журнала в файле

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("hi", hello_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()

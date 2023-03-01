from typing import Dict
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [
    ["чтение", "запись"],
    ["поиск", "изменение"],
    ["удаление", "выход"],
]

characteristic_keyboard = [
    ["id", "фамилия"],
    ["имя", "отчество"],
    ["номер", "отмена"],
]

confirmation_keyboard = [
    ["да", "нет"],
]

cancel_keyboard = [
    ["отмена"],
]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
characteristic_markup = ReplyKeyboardMarkup(characteristic_keyboard, one_time_keyboard=True)
confirmation_markup = ReplyKeyboardMarkup(confirmation_keyboard, one_time_keyboard=True)
cancel_markup = ReplyKeyboardMarkup(cancel_keyboard, one_time_keyboard=True)

file_name = 'phone_book.txt'


def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask user for input."""

    try:
        file = open(file_name, 'r')
    except IOError:
        file = open(file_name, 'w')
    finally:
        file.close()

    context.user_data["confirmation"] = False

    await update.message.reply_text('Какое действие хотите совершить?', reply_markup=markup)

    return CHOOSING


async def new_records(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["choice"] = 'запись'
    await update.message.reply_text('Введите фамилию, имя, отчество, номер телефона через пробел'
                                    , reply_markup=cancel_markup)

    return TYPING_REPLY


async def print_records(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(file_name, 'r', encoding='utf-8') as data:
        text = ''.join(data).replace(';', ' ')
        await update.message.reply_text(text, reply_markup=markup) if text != '' \
            else await update.message.reply_text('Телефонная книжка пуста', reply_markup=markup)

    return CHOOSING


async def confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == 'да':
        if context.user_data['choice'] == 'изменение':
            await update.message.reply_text('Введите фамилию, имя, отчество, номер телефона через пробел')
        else:
            context.user_data["confirmation"] = False
            replace_record_line(context.user_data['record_id'], '')
            await update.message.reply_text('Какое действие хотите совершить?', reply_markup=markup)
            return CHOOSING
    else:
        context.user_data["confirmation"] = False
        await update.message.reply_text('Введите id записи', reply_markup=cancel_markup)

    return TYPING_REPLY


characteristics = {'id': '0',
                   'фамилия': '1',
                   'имя': '2',
                   'отчество': '3',
                   'номер': '4'}


async def received_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    text = update.message.text
    category = user_data["choice"]
    if category == "запись":
        input_record(text)
    elif category == "поиск":
        characteristic = user_data["characteristic"]
        await update.message.reply_text(find_records(characteristics[characteristic], text))
    elif category in ["изменение", "удаление"]:
        if not context.user_data["confirmation"]:
            text_add = "изменить" if category == "изменение" else "удалить"
            context.user_data['record_id'] = text
            text = find_records('0', context.user_data['record_id'])
            if text == "Не найдено":
                await update.message.reply_text(text)
            else:
                await update.message.reply_text(f"Вы хотите {text_add} данную запись?",
                                                reply_markup=confirmation_markup)
                await update.message.reply_text(text)
                context.user_data["confirmation"] = True
            return CHOOSING
        else:
            text = f'{int(context.user_data["record_id"])};' + (';'.join(text.split()[:4]) + '\n')
            replace_record_line(context.user_data['record_id'], text)
            context.user_data["confirmation"] = False

    await update.message.reply_text('Какое действие хотите совершить?', reply_markup=markup)

    return CHOOSING


def input_record(text):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        text = f'{int(record_id) + 1};' + ';'.join(text.split()[:4])
        data.write(text + '\n')


async def find_records_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["choice"] = 'поиск'
    await update.message.reply_text('Выберите характеристику:', reply_markup=characteristic_markup)
    return CHOOSING


async def find_characteristic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    context.user_data["characteristic"] = text
    await update.message.reply_text('Введите значение характеристики', reply_markup=cancel_markup)
    return TYPING_REPLY


def find_records(characteristic, condition):
    text = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            if condition == line.split(';')[int(characteristic)].replace('\n', ''):
                text += line.replace(';', ' ')
    if text == '':
        text = "Не найдено"
    return text


async def change_record_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["choice"] = 'изменение'
    await update.message.reply_text('Введите id записи', reply_markup=cancel_markup)
    return TYPING_REPLY


def replace_record_line(record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)


async def delete_record(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["choice"] = 'удаление'
    await update.message.reply_text('Введите id записи', reply_markup=cancel_markup)
    return TYPING_REPLY


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Display the gathered info and end the conversation."""
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]
    if "characteristic" in user_data:
        del user_data["characteristic"]
    if "confirmation" in user_data:
        del user_data["confirmation"]

    await update.message.reply_text(
        "Работа программы закончена",
        reply_markup=ReplyKeyboardRemove(),
    )

    user_data.clear()
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("TOKEN").build()

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [
                MessageHandler(
                    filters.Regex("^(чтение)$"), print_records
                ),
                MessageHandler(
                    filters.Regex("^(запись)$"), new_records
                ),
                MessageHandler(
                    filters.Regex("^(поиск)$"), find_records_start
                ),
                MessageHandler(
                    filters.Regex("^(изменение)$"), change_record_start
                ),
                MessageHandler(
                    filters.Regex("^(удаление)$"), delete_record
                ),
                MessageHandler(
                    filters.Regex("^(да|нет)$"), confirmation
                ),
                MessageHandler(
                    filters.Regex("^(id|фамилия|имя|отчество|номер)$"), find_characteristic
                ),
                MessageHandler(
                    filters.Regex("^(отмена)$"), start
                ),
            ],
            TYPING_REPLY: [
                MessageHandler(
                    filters.Regex("^(отмена)$"), start
                ),
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^выход$")),
                    received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^выход$"), done)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()

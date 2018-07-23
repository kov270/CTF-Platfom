from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
from keyboards.category_keyboard import category_markup
from keyboards.main_keyboard import main_markup
from keyboards.task_keyboard import tasks


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = ""
ADMIN_ID = 167067147


def start(bot, update):
    update.message.reply_text("Привет, это CTF", reply_markup=main_markup)
    return update.message.text


def task(bot, update):
    update.message.reply_text("Здесь должны быть таски с inline кнопочками", reply_markup=category_markup)


def inline_button(bot, update):
    query = update.callback_query
    task_markup = tasks(query.data)
    bot.edit_message_reply_markup(reply_markup=task_markup,
                                  chat_id=query.message.chat_id,
                                  message_id=query.message.message_id)


if __name__ == "__main__":
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('tasks', task))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_button))
    updater.start_polling()

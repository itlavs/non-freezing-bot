from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Добрый день, вечер, ночь или утро.\n"
                          "Нужна вам незамерзайка?(незамерзающая стеклоомывающая жидкость).\n"
                          "Я ваш персональный менеджер и готов принять Ваш заказ.")


def text(bot, update):
    response = "Вы написали: " + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


def command(bot, update):
    response = "Вы написали: " + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


updater = Updater(token='1453435374:AAEzcH7rmrT8knnAHH6UwEY2X55zTDSTpsY')
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
text_handler = MessageHandler(Filters.text, text)
command_handler = MessageHandler(Filters.command, command)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)
dispatcher.add_handler(command_handler)
updater.start_polling(clean=True)
updater.idle()

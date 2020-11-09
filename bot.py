from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# import apiai, json

updater = Updater(token='<ТОКЕН ТЕЛЕГРАМА>')
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Добрый день, вечер, ночь или утро.\n"
                          "Нужна вам незамерзайка?(незамерзающая стеклоомывающая жидкость).\n"
                          "Я ваш персональный менеджер и готов принять Ваш заказ.")


def textMessage(bot, update):
    response = "Вы написали: " + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

    # request = apiai.ApiAI('ТОКЕН DialogFlow').text_request()
    # request.lang = 'ru'
    # request.session_id = '<ИДЕНТИФИКАТОР В DialogFlow>'
    # request.query = update.message.text
    #
    # responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    # response = responseJson['result']['fulfillment']['speech']
    # if response:
    #     bot.send_message(chat_id=update.message.chat_id, text=response)
    # else:
    #     bot.send_message(chat_id=update.message.chat_id, text="Не понял вас.")


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()

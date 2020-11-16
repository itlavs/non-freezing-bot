from .bot import *

bot_token = ''

if __name__ == "__main__":
    bot = Bot(bot_token, dialog)
    bot.start()

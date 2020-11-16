from .bot import *

bot_token = '1453435374:AAEzcH7rmrT8knnAHH6UwEY2X55zTDSTpsY'

if __name__ == "__main__":
    bot = Bot(bot_token, dialog)
    bot.start()
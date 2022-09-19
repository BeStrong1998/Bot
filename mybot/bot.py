
from tokenize import maybe
from unicodedata import name
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

import setings

#PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def talk_to_me(updata, context):
    text = updata.message.text
    print(text)
    updata.message.reply_text(text)

def main():
    maybe = Updater(setings.API_KEY, use_context=True) #request_kwargs=PROXY)

    dp = maybe.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    maybe.start_polling()
    maybe.idle()

if __name__ == '__main__':
    main()

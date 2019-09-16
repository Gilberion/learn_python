from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import logging
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
    )

def greet_user(bot, update):
    text = 'Старт!'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text) 
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
    update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planet(bot, update):
    date = datetime.date.today()
    text_at = update.message.text.split(' ')[1].capitalize()
    if text_at == 'Sun':
        const = ephem.constellation(ephem.Sun(date))
    elif text_at == 'Mercury':
        const = ephem.constellation(ephem.Mercury(date))
    elif text_at == 'Venus':
        const = ephem.constellation(ephem.Venus(date))
    elif text_at == 'Earth':
        const = 'Неизвестная планета'
    elif text_at == 'Moon':
        const = ephem.constellation(ephem.Mars(date))   
    elif text_at == 'Mars':
        const = ephem.constellation(ephem.Mars(date))
    elif text_at == 'Jupiter':
        const = ephem.constellation(ephem.Jupiter(date))
    elif text_at == 'Saturn':
        const = ephem.constellation(ephem.Saturn(date))
    elif text_at == 'Uranus':
        const = ephem.constellation(ephem.Uranus(date))
    elif text_at == 'Neptune':
        const = ephem.constellation(ephem.Neptune(date))
    elif text_at == 'Pluto':
        const = ephem.constellation(ephem.Pluto(date))
    else:
        const = 'Данные не доступны'
    update.message.reply_text(const)
         
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()
    


main()
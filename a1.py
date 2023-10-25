import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as b


bot = telebot.TeleBot('6961677992:AAEJIq_-hrYOH6b0u1EXwZirjUt9On8EkCc')


def get_inf(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')

    news_items = soup.find_all('div', class_='se-material__title se-material__title--size-middle')
    timings = soup.find_all('div', class_='se-news-list-page__item-left')
    news_heads = [c.text for c in news_items][:3]
    links = [c.find_all('a') for c in news_items][:3]
    timing_list = [c.text for c in timings][:3]

    ans = []
    for j in range(3):
        if len(timing_list[j].split()) == 1:
            date = timing_list[j].strip() + ' (сегодня)'
        else:
            ind = timing_list[j].find(':') + 3
            date = timing_list[j][:ind] + f' ({timing_list[j][ind:ind + 6].strip()})'
        head = news_heads[j].strip()
        text = str(links[j][0]).split('"')[1]
        ans.append([date, head, text])
    return ans[::-1]


@bot.message_handler(commands=['start'])
def button(message):
    bot.send_message(message.chat.id, 'Привет! Я бот cпортивных новостей. \nИспользуйте команду */sport* или */cyber* для просмотра последних *спортивных* или *игровых* событий соответсвенно.', parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'q_1':
            URL = 'https://www.sport-express.ru/football/news/?isEditorialChoice=1'
            inf = get_inf(URL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= f'{inf[0][0]} \n{inf[0][1]} \n{inf[0][2]}')
            inf = inf[1:]
            for l in inf:
                bot.send_message(call.message.chat.id, f'{l[0]} \n{l[1]} \n{l[2]}', parse_mode="Markdown")
        elif call.data == 'q_2':
            URL = 'https://www.sport-express.ru/hockey/news/?isEditorialChoice=1'
            inf = get_inf(URL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'{inf[0][0]} \n{inf[0][1]} \n{inf[0][2]}')
            inf = inf[1:]
            for l in inf:
                bot.send_message(call.message.chat.id, f'{l[0]} \n{l[1]} \n{l[2]}', parse_mode="Markdown")
        elif call.data == 'q_3':
            URL = 'https://www.sport-express.ru/basketball/news/?isEditorialChoice=1'
            inf = get_inf(URL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'{inf[0][0]} \n{inf[0][1]} \n{inf[0][2]}')
            inf = inf[1:]
            for l in inf:
                bot.send_message(call.message.chat.id, f'{l[0]} \n{l[1]} \n{l[2]}', parse_mode="Markdown")
        elif call.data == 'q_c_1':
            URL = 'https://www.sport-express.ru/cybersport/dota2/news/'
            inf = get_inf(URL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'{inf[0][0]} \n{inf[0][1]} \n{inf[0][2]}')
            inf = inf[1:]
            for l in inf:
                bot.send_message(call.message.chat.id, f'{l[0]} \n{l[1]} \n{l[2]}', parse_mode="Markdown")
        elif call.data == 'q_c_2':
            URL = 'https://www.sport-express.ru/cybersport/csgo/news/'
            inf = get_inf(URL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'{inf[0][0]} \n{inf[0][1]} \n{inf[0][2]}')
            inf = inf[1:]
            for l in inf:
                bot.send_message(call.message.chat.id, f'{l[0]} \n{l[1]} \n{l[2]}', parse_mode="Markdown")
        elif call.data == 'q_c_3':
            URL = 'https://www.sport-express.ru/cybersport/league-of-legends/news/'
            inf = get_inf(URL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'{inf[0][0]} \n{inf[0][1]} \n{inf[0][2]}')
            inf = inf[1:]
            for l in inf:
                bot.send_message(call.message.chat.id, f'{l[0]} \n{l[1]} \n{l[2]}', parse_mode="Markdown")


@bot.message_handler(commands=['sport'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Последние новости Футбола', callback_data='q_1')
    item2 = types.InlineKeyboardButton('Последние новости Хоккея', callback_data='q_2')
    item3 = types.InlineKeyboardButton('Последние новости Баскетбола', callback_data='q_3')
    markup.add(item, item2, item3)

    bot.send_message(message.chat.id, 'Вы можете выбрать:',
                     reply_markup=markup)


@bot.message_handler(commands=['cyber'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Последние новости Dota 2', callback_data='q_c_1')
    item2 = types.InlineKeyboardButton('Последние новости CS:GO', callback_data='q_c_2')
    item3 = types.InlineKeyboardButton('Последние новости League of Legends', callback_data='q_c_3')
    markup.add(item, item2, item3)

    bot.send_message(message.chat.id, 'Вы можете выбрать:',
                     reply_markup=markup)


bot.infinity_polling()

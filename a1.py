import telebot
from telebot import types

bot = telebot.TeleBot('6961677992:AAEJIq_-hrYOH6b0u1EXwZirjUt9On8EkCc')

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Недавние спортивные события.', callback_data='q_1')
    item2 = types.InlineKeyboardButton('Ближайшие спортивные события.', callback_data='q_2')
    item3 = types.InlineKeyboardButton('Грядущие спортивные события.', callback_data='q_3')
    markup.add(item, item2, item3)
 
    bot.send_message(message.chat.id, 'Привет! Я бот cпортивных новостей. Какие новости тебя интересуют:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'q_1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'IEM Fall 2023 - c 16 по 22 октября: https://www.cybersport.ru/tags/cs2/raspisanie-i-rezultaty-iem-sydney-2023?_gl=1%2a5qtjl2%2a_ga%2aWDVfdmZBeDB0blN6WU41OW9JamRUeF9ZdTJobmlWc2Z3eEw5OUdoTDRuZ1oyeGF0cjBKdTFFZXppNGZmMktLQg..')
            bot.send_message(message.chat.id, 'Привет! Я бот cпортивных новостей. Какие новости тебя интересуют:', reply_markup=markup)
        elif call.data == 'q_2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'BLAST Premier Fall Final 2023 - С 22 по 26 ноября: https://www.cybersport.ru/tournaments/cs2/blast-premier-fall-final-2023-1')
            bot.send_message(message.chat.id, 'Привет! Я бот cпортивных новостей. Какие новости тебя интересуют:', reply_markup=markup)
        elif call.data == 'q_3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Вставь текст №3')
            bot.send_message(message.chat.id, 'Привет! Я бот cпортивных новостей. Какие новости тебя интересуют:', reply_markup=markup)
 
bot.infinity_polling()

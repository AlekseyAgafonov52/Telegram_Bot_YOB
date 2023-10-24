import telebot

bot = telebot.TeleBot('6961677992:AAEJIq_-hrYOH6b0u1EXwZirjUt9On8EkCc')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')


@bot.message_handler(commands=['events_last_week'])
def main(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['events_todays'])
def main(message):
    bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['events_next_week'])
def main(message):
    bot.send_message(message.chat.id, '')


bot.infinity_polling()

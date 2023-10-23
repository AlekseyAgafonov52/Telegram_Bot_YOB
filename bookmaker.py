import telebot

bot = telebot.TeleBot('6961677992:AAEJIq_-hrYOH6b0u1EXwZirjUt9On8EkCc')


@bot.message_handler(commands=['start', 'events'])
def main(message):
    bot.send_message(message.chat.id, 'hello')


bot.infinity_polling()

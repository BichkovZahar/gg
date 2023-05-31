import telebot
import random
from telebot import types
import wikipedia
clays = wikipedia.summary(random.choice(['Summer' , 'Wikipedia' , 'Nature']))
if len(clays) >= 1000:
        print(clays)
else:
    print(f"Немає")

bot = telebot.TeleBot("6163752027:AAGlnVbZFdz8HWWnjdykXcOMLrkUwYixdrA")

@bot.message_handler(commands=['start'])
def start(m):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Пуск")
    markup.add(item1)
    bot.send_message(m.chat.id, "Нажміть", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == "Пуск":
        answer = f"{clays}"
    bot.send_message(message.chat.id, answer)
bot.polling()
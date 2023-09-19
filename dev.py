import telebot
from telebot import types
from telebot import callback_data

bot = telebot.TeleBot('6467407681:AAF37eHg6bAY6-v90GhmlxQDg3YqD3n-XXQ')

name = ''
surname = ''
age = 0
photo_us = ''


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Добро пожаловать! Этот бот для создания резюме. Чтобы собрать резюме нам необходимо заполнить сдежующие обязательные поля:')
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Давай зарегестрируемся с помощью команды /reg')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    try:
        age = int(message.text)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_yes, key_no)
        question = f'Тебе {age} лет, тебя зовут {name} {surname}?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    except ValueError:
        bot.send_message(message.from_user.id, 'Пожалуйста, введите возраст цифрами.')

@bot.callback_query_handler(func=lambda call: True)
def question(call):
    if call.data == 'yes':
        bot.register_next_step_handler(message, get_photo)
    elif call.data == 'no':
        bot.send_message(message, 'Давай начнем заново.')
        start(call.data)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    global photo_us
    photo = max(message.photo, key=lambda x: x.height)
    print(photo.file_id)


bot.polling(non_stop=True, interval=0)

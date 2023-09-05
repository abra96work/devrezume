import telebot
from telebot import types

bot = telebot.TeleBot('6467407681:AAF37eHg6bAY6-v90GhmlxQDg3YqD3n-XXQ')

# @bot.message_handler(content_types=['text'])
# def get_text_message(message):
#     if message.text == 'Привет':
#         bot.send_message(message.from_user.id, 'Для старта работы напиши /reg')
#     elif message.text == '/help':
#         bot.send_message(message.from_user.id, 'Напиши "Привет"')
#     else:
#         bot.send_message(message.from_user.id, 'Я тебя не понимаю, напиши "Привет"')


name = '';
surname = '';
age = 0;

@bot.message_handler(commands=['button'])
def welcome(message):
    keyboard_start = types.InlineKeyboardMarkup();
    key_start = types.InlineKeyboardButton(text='Начать работу', callback_data='start');
    keyboard_start.add(key_start);
    if call.data == 'start':
        start()

@bot.message_handler(content_types = ['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Давай зарегестрируемся с помощью команды /reg');
        
def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age);

@bot.message_handler(commands=['button'])
def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введи числоовое значение')
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
    keyboard.add(key_yes);
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тебе {age} лет, тебя зовут {name} {surname}?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    if call.data == 'yes':
        bot.send_message(message.from_user.id, 'Запомню')
    elif call.data == 'no':
        start()

# @bot.message_handler(commands=['button'])
# def button_quest(message):
#     keyboard = types.InlineKeyboardMarkup();
#     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
#     keyboard.add(key_yes);
#     key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
#     keyboard.add(key_no);
#     question = 'Тебе {age} лет, тебя зовут {name} {surname}?'
#     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#     if call.data == 'yes':
#         bot.send_message(message.from_user.id, 'Запомню')
#     elif call.data == 'no':
#         start()

bot.polling(non_stop=True, interval=0)

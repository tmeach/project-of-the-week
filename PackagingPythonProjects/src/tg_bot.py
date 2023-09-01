import telebot
from currency_converter import CurrencyConverter
from telebot import types

# Настройки для Telegram бота
my_token = '***' # put your personal token here 
bot = telebot.TeleBot(token=my_token)
chat_id = '***' # put your chat_id here

currency = CurrencyConverter()
amount = 0 


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! Enter the amount:')
    bot.register_next_step_handler(message, summa)
    
def summa(message):
    global amount
    try:
        amount = int(message.text.strip()) 
    except ValueError:
        bot.send_message(message.chat.id, 'The format is wrong. Try again:')
        bot.register_next_step_handler(message, summa)
        return
    
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GDP', callback_data='usd/gdp')
        btn4 = types.InlineKeyboardButton('Other', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Pick your pair', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'The number must be greater than 0. Enter the amount:')
        bot.register_next_step_handler(message, summa)
        
        
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'The result: {round(res,2)}. You can enter the amount again')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Enter a pair of values via /')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'The result: {round(res,2)}. You can enter the amount again')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Something wrong. Enter the value again')
        bot.register_next_step_handler(message, my_currency)
        
    
import telebot
import pytest
from tg_bot import start, summa, callback, my_currency


# Create pytest fixture
@pytest.fixture
def bot_instance():
    my_token = '***'  # add your tokem
    return telebot.TeleBot(token=my_token)

# Testing start function 
def test_start(bot_instance):
    message = telebot.types.Message()
    message.chat.id = 123  # Замените на ваш chat_id
    start(message)
  
# Testing summa function 
def test_summa(bot_instance):
    message = telebot.types.Message()
    message.text = "100"  # Предположим, что это корректный ввод
    message.chat.id = 123  # Замените на ваш chat_id
    summa(message)

# Testing callback function 
def test_callback(bot_instance):
    call = telebot.types.CallbackQuery()
    call.data = 'usd/eur'  # Предположим, что это корректный ввод
    call.message = telebot.types.Message()
    call.message.chat.id = 123  # Замените на ваш chat_id
    callback(call)

# Testing my_currency function 
def test_my_currency(bot_instance):
    message = telebot.types.Message()
    message.text = "USD/EUR"  # Предположим, что это корректный ввод
    message.chat.id = 123  # Замените на ваш chat_id
    my_currency(message)
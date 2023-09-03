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
    message.chat.id = 123  # put your chat_id
    start(message)
   
    # Mocking bot send message 
    mocker.patch.object(bot_instance, 'send_message')
    start(message)
    
    # Check that bot send message with text "Hello! Enter the amount:"
    bot_instance.send_message.assert_called_once_with(message.chat.id, 'Hello! Enter the amount:')
   
    # checking the registered processor
    bot_instance.register_next_step_handler.assert_called_once()

# Testing summa function 
def test_summa(bot_instance):
    message = telebot.types.Message()
    message.text = "100"
    message.chat.id = 123  # put your chat_id
    
    # Mocking bot send message and register handler
    mocker.patch.object(bot_instance, 'send_message')
    mocker.patch.object(bot_instance, 'register_next_step_handler')
    
    summa(message)
    
    # Checking that bot send message with KeyBoard
    bot_instance.send_message.assert_called_once()
    args, kwargs = bot_instance.send_message.call_args
    assert isinstance(kwargs['reply_markup'], telebot.types.InlineKeyboardMarkup)

    # Checking that bot register handler
    bot_instance.register_next_step_handler.assert_called_once()
    
    # Cheking that amount is correct 
    assert amount == 100  

# Testing callback function 
def test_callback(bot_instance, mocker):
    call = telebot.types.CallbackQuery()
    call.data = 'usd/eur'  
    call.message = telebot.types.Message()
    call.message.chat.id = 123  # put your chat_id

    # Mocking bot send message and register handler
    mocker.patch.object(bot_instance, 'send_message')
    mocker.patch.object(bot_instance, 'register_next_step_handler')

    callback(call)

    # Checking that bot send message with convert result
    bot_instance.send_message.assert_called_once()
    args, kwargs = bot_instance.send_message.call_args
    assert "The result" in kwargs['text']

    # Checking that bot register handler
    bot_instance.register_next_step_handler.assert_called_once()

    # Cheking the register processor
    args, kwargs = bot_instance.register_next_step_handler.call_args
    assert args[1] == summa  

# Testing my_currency function 
def test_my_currency(bot_instance, mocker):
    message = telebot.types.Message()
    message.text = "USD/EUR" 
    message.chat.id = 123  # Put your chat_id

    # Mocking bot send message and register handler
    mocker.patch.object(bot_instance, 'send_message')
    mocker.patch.object(bot_instance, 'register_next_step_handler')

    my_currency(message)

    # Checking that bot send message with convert result
    bot_instance.send_message.assert_called_once()
    args, kwargs = bot_instance.send_message.call_args
    assert "The result" in kwargs['text']

    # Checking that bot register handler
    bot_instance.register_next_step_handler.assert_called_once()

    # Cheking the register processor
    args, kwargs = bot_instance.register_next_step_handler.call_args
    assert args[1] == summa  
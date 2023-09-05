import telebot
import pytest
import config
from tg_bot import start  # Замените 'your_module' на имя вашего модуля
from telebot.types import Message, Chat
from unittest.mock import MagicMock

# Фикстура для создания объекта чата
@pytest.fixture
def chat():
    return Chat(id=config.CHAT_ID, type='private')  # Замените 123 на ваш chat_id

# Фикстура для создания объекта сообщения
@pytest.fixture
def message(chat):
    return Message(
        message_id=1,
        from_user=None,
        date=None,
        chat=chat,
        content_type='text',
        options=[],
        json_string=None
    )

# Фикстура для создания объекта бота
@pytest.fixture
def bot():
    return telebot.TeleBot(token=config.BOT_TOKEN)  # Замените 'your_token_here' на ваш токен

# Мокируем функцию send_message бота
@pytest.fixture
def mock_send_message(bot):
    bot.send_message = MagicMock()

def test_start_message(bot, message, mock_send_message):
    start(message)
    assert bot.send_message.called_once_with(message.chat.id, 'Hello! Enter the amount:')

def test_start_message_with_non_positive_amount(bot, message, mock_send_message):
    message.text = '0'
    start(message)
    assert bot.send_message.called_once_with(message.chat.id, 'The number must be greater than 0. Enter the amount:')

def test_start_message_with_invalid_amount(bot, message, mock_send_message):
    message.text = 'abc'
    start(message)
    assert bot.send_message.called_once_with(message.chat.id, 'The format is wrong. Try again:')

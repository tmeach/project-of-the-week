import telebot
import pytest
from unittest.mock import Mock
from tg_bot import summa, my_currency

# Создаем мок-объект для бота и сообщения
bot = Mock(spec=telebot.TeleBot)
message = Mock(spec=telebot.types.Message)

# Устанавливаем атрибут chat для объекта message
chat = Mock()
message.chat = chat

# Тестирование функции summa
def test_summa_with_valid_amount():
    # Устанавливаем текст сообщения
    message.text = '100'  # Ваше допустимое значение
    expected_reply = 'Pick your pair'  # Ожидаемый ответ бота

    # Вызываем функцию summa
    summa(message)

    # Проверяем, что бот отправил ожидаемый ответ
    bot.send_message.assert_called_once_with(chat.id, expected_reply)

def test_summa_with_invalid_amount():
    # Устанавливаем текст сообщения с недопустимым значением
    message.text = 'abc'  # Недопустимое значение
    expected_reply = 'The format is wrong. Try again:'  # Ожидаемый ответ бота

    # Вызываем функцию summa
    summa(message)

    # Проверяем, что бот отправил ожидаемый ответ
    bot.send_message.assert_called_once_with(chat.id, expected_reply)

# Тестирование функции my_currency
def test_my_currency_with_valid_input():
    # Устанавливаем текст сообщения с допустимым вводом
    message.text = 'USD/EUR'  # Ваше допустимое значение
    expected_reply = 'The result: 1.0. You can enter the amount again'  # Ожидаемый ответ бота

    # Вызываем функцию my_currency
    my_currency(message)

    # Проверяем, что бот отправил ожидаемый ответ
    bot.send_message.assert_called_once_with(chat.id, expected_reply)

def test_my_currency_with_invalid_input():
    # Устанавливаем текст сообщения с недопустимым вводом
    message.text = 'invalid_input'  # Недопустимый ввод
    expected_reply = 'Something is wrong. Enter the value again'  # Ожидаемый ответ бота

    # Вызываем функцию my_currency
    my_currency(message)

    # Проверяем, что бот отправил ожидаемый ответ
    bot.send_message.assert_called_once_with(chat.id, expected_reply)

from telebot import types


start = types.ReplyKeyboardMarkup(True, False)
start.add("Let's play!")


numbers = types.ReplyKeyboardMarkup(row_width=5)
numbers.add('1', '2', '3', '4', '5')
numbers.add('6', '7', '8', '9', '10')

# -*- coding: utf-8 -*-

import telebot

import guess as game
from settings import BOT_TOKEN
from menu import start, numbers


bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')
guess_game = game.GuessGame()


@bot.message_handler(commands=['start'])
def start_game(message):
    global guess_game
    if guess_game.isPlayable():
        bot.reply_to(message, guess_game.start_game())
        bot.send_message(
            message.chat.id, "Guess number by choosing one of the following numbers:", reply_markup=numbers)
    else:
        bot.send_message(
            message.chat.id, "👋 Hi! I came up with a number, do you want to try to guess it?", reply_markup=start)


@bot.message_handler(content_types=['text'])
def main(message):
    global guess_game
    if message.text == "Let's play!":
        bot.send_message(
            message.chat.id, guess_game.start_game(), reply_markup=numbers)
    else:
        try:
            result = guess_game.guess_number(int(message.text))
            if result == True:
                bot.send_message(
                    message.chat.id, "🎉 You've won!", reply_markup=start)
            if result == False:
                bot.send_message(
                    message.chat.id, "😭 You've lost(((", reply_markup=start)
            else:
                if result != True:
                    bot.send_message(message.chat.id, result, reply_markup=numbers)
        except Exception as e:
            print(e)
            bot.send_message(
                message.chat.id, "Guess number by choosing one of the following numbers:", reply_markup=numbers)


if __name__ == '__main__':
    bot.polling()

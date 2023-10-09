from aiogram import types

buttons = [[types.InlineKeyboardButton(text='Give Lottery Number', web_app=types.WebAppInfo(url='https://javabestfullcoder.github.io/TelegramLoteryBot/'))]]

markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)

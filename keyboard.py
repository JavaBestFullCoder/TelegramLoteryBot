from aiogram import types

buttons = [[types.InlineKeyboardButton(text='Open Lotery', web_app=types.WebAppInfo(url='index.html'))]]

markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)
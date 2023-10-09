from aiogram import types

buttons = [[types.InlineKeyboardButton(text='Open Lotery', web_app=types.WebAppInfo(url='https://github.com/c418f853-b820-46a7-b9cc-df72bb98c4b6'))]]

markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)

from aiogram import types

buttons = [[types.InlineKeyboardButton(text='Open Lotery', web_app=types.WebAppInfo(url='https://github.com/JavaBestFullCoder/TelegramLoteryBot/blob/ddcb74986b8bf2db3e18b31fd90de20d00563091/index.html'))]]

markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)

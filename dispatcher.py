import logging

from aiogram import Bot, Dispatcher, types

import config


# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not config.BOT_TOKEN:
    exit("No token provided")

#proxy = 'http://192.168.42.129:8080'

# init
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
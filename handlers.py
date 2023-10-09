import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

import config
import db.database
from aiogram.types import Message
from States import Stat as Stat
import keyboard
from dispatcher import bot

router = Router()

db = db.database.ControllerDB("db/data.db")


# def for check, can str cast to int
async def is_castable_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


async def is_lottery_vinner(allusers):
    users_numbs = []
    for user in allusers:
        users_numbs.append(user[2])

    rand_vinner = random.choice(users_numbs)
    return db.get_us_by_numb(rand_vinner)





# Filter, if user State is "numb"
@router.message(Stat.numb)
async def get_numb(message: Message, state: FSMContext):
    number = message.text
    if await is_castable_to_int(number):
        if int(number) != 0:
            db.upd_numb(number, message.from_user.id)
            await message.answer(
                f"Good Job! You participate in the lottery under the number:{number}\n\n*<i>Every day at 12:00 Moscow time, a draw is held, you will receive a message if you win!</i>")
            await state.clear()
        else:
            await message.answer("You dont send your lottery number(")
    else:
        await message.answer("You dont send your lottery number(")


# Filter, if message is command "/start"
@router.message(Command('start'))
async def start_handler(message: Message, state: FSMContext):
    # add user to database
    if not db.user_exist(message.from_user.id):
        db.add_user(message.from_user.id)
    # send Hello message
    await message.answer("Hello! Give your number here:\n\n*<i>Before giving, send your number to this chat</i>",
                         reply_markup=keyboard.markup)
    await state.set_state(Stat.numb)


# Handle all messages
@router.message()
async def message_handler(message: Message):
    if message.from_user.id in config.ADMIN_ID:
        if message.text == '/lot':
            vinner_id = await is_lottery_vinner(db.get_users())
            await bot.send_message(chat_id=vinner_id, text="Congrats! YOU WON 1.000.000$ !!!!")
    else:
        await message.answer("Unaccepted Command!")

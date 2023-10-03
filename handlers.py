from aiogram import types, Router
from aiogram.filters import Command


from aiogram.types import Message, ChatJoinRequest, CallbackQuery

import keyboard

router = Router()


@router.message(Command('start'))
async def start_handler(message: Message):
    await message.answer("For Lottery Open he:", reply_markup=keyboard.markup)
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.defolt import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Добро пожаловать, {message.from_user.full_name}!\n Я - <b>СтудХелпер</b>, твой личный помощник в выборе самого лучшего и вкусного:)", reply_markup=menu)

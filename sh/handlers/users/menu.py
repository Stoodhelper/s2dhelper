from loader import dp
from aiogram.types import Message
from keyboards.defolt import menu
from keyboards.inline import eda
from aiogram.dispatcher.filters import Command,Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


#@dp.message_handler(Command("Menu"))
#async def show_menu(message:Message):
#    await message.answer("Viberete",reply_markup=menu)
#@dp.message_handler(text="Еда 🍏")
#async def eat(message:Message):
#    await message.answer("VIBIRI,",reply_markup=eda)
#@dp.message_handler(Command("Все категории"))
#async def all(message: Message):
 #   await message.answer(text="На продажу у нас есть 2 товара: 5 Яблок и 1 Груша. \n"
  #                            "Если вам ничего не нужно - жмите отмену",
   #                      reply_markup=eda)
#@dp.message_handler(Text(equals=["Еда","Все категории","Лайфхак"]))
#async def get_food(message:Message):
#    await message.answer(f"Vi vibrali {message.text}.",parse_mode='html',
 #                        reply_markup=eda)

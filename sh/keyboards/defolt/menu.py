from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Еда 🍏"),
        KeyboardButton(text="Лайфхаки и халява 👌")
        ],
        [KeyboardButton(text="Корзина 🛒"),
        KeyboardButton(text="Все категории")
         ],
        [KeyboardButton(text="Книга жалоб и предложений ✍"),
        KeyboardButton(text="Поддержать проект 🆘")
        ]
    ],
        resize_keyboard=True
)
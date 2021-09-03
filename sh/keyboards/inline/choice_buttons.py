from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_APPLES, URL_PEAR,URL_news
from keyboards.inline.callback_datas import buy_callback

# Вариант 2 - с помощью row_width и insert.
choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

###

eda=InlineKeyboardMarkup(row_width=1)
eda1=InlineKeyboardButton(text='Просто, за вкусняшками',callback_data="vkus")
eda2=InlineKeyboardButton(text='Продукты, готовить',callback_data='product')
eda3=InlineKeyboardButton(text='Рецепты',callback_data='recipes')
eda4=InlineKeyboardButton(text='Вообще не знаю(',callback_data='xz')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
eda.add(eda1,eda2,eda3,eda4,back)
###

vkus=InlineKeyboardMarkup(row_width=1)
v1=InlineKeyboardButton(text='Прямо сейчас',callback_data='now')
v2=InlineKeyboardButton(text='Есть время приготовить',callback_data='time')
kat=InlineKeyboardButton(text='Выбрать раздел магазина',callback_data='choose')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
vkus.add(v1,v2,kat,back)
###

skils=InlineKeyboardMarkup(row_width=1)
s1=InlineKeyboardButton(text='Легко',callback_data='easy')
s2=InlineKeyboardButton(text='Трудно',callback_data='hard')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
skils.add(s1,s2,back)
###

ed=InlineKeyboardMarkup(row_width=1)
eat=InlineKeyboardButton(text='Поесть',callback_data='eat')
drink=InlineKeyboardButton(text='Попить',callback_data='drink')
kat=InlineKeyboardButton(text='Выбрать раздел магазина',callback_data='choose')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
ed.add(eat,drink,kat,back)
###

eatO=InlineKeyboardMarkup(row_width=2)
ea1=InlineKeyboardButton(text='Похрустеть и т.п.🍿',callback_data='hrust')
ea2=InlineKeyboardButton(text='Перекусить🍔',callback_data='kus')
ea3=InlineKeyboardButton(text='Что-то необычное🔮',callback_data='wow')
kat=InlineKeyboardButton(text='Выбрать раздел магазина',callback_data='choose')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
eatO.add(ea1,ea2,ea3,kat,back)
drin=InlineKeyboardMarkup(row_width=2)
d1 = InlineKeyboardButton(text='Газировка',callback_data='gas')
d2 = InlineKeyboardButton(text='Сок',callback_data='sok')
d3 = InlineKeyboardButton(text='Энергетики',callback_data='energy')
d4 = InlineKeyboardButton(text='Алькоголь',callback_data='alcogol')
kat=InlineKeyboardButton(text='Выбрать раздел магазина',callback_data='choose')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
drin.add(d1,d2,d3,d4,kat,back)
###

lifehack=InlineKeyboardMarkup(row_width=2)
lh1=InlineKeyboardButton(text='Халява и купоны 💸',callback_data='free')
lh2=InlineKeyboardButton(text='Куда сходить в МСК 🌇',callback_data='msk')
lh3=InlineKeyboardButton(text='Залипательные сайты',callback_data='site')
lh4=InlineKeyboardButton(text='Шутки и анекдоты',callback_data='joke')
lifehack.add(lh1,lh2,lh3,lh4)
###
free=InlineKeyboardMarkup(row_width=1)
f1 = InlineKeyboardButton(text='Еда',callback_data='feat')
f2 = InlineKeyboardButton(text='Доставка',callback_data='dilivery')
f3 = InlineKeyboardButton(text='Такси',callback_data='taxi')
f4 = InlineKeyboardButton(text='Каршеринг',callback_data='shcar')
free.add(f1,f2,f3,f4)
###
msk=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=' Лучшие 50 мест в Москве от Куда GO',url=URL_news)],
    InlineKeyboardButton(text='Метса обязательного посещения в МСК', url=URL_news)]
)
kat=InlineKeyboardMarkup(row_width=3)
k1 = InlineKeyboardButton(text="Овощи и фрукты", callback_data='fruit')
k2 = InlineKeyboardButton(text="Молочка", callback_data='milk')
k3 = InlineKeyboardButton(text="Приправы и мелочь", callback_data='small')
k4 = InlineKeyboardButton(text="К чаю", callback_data='tea')
k5 = InlineKeyboardButton(text="Химия и др.", callback_data='other')
k6 = InlineKeyboardButton(text="Особенное", callback_data='wow')
k7 = InlineKeyboardButton(text="На каждый день", callback_data='defolt')
k8 = InlineKeyboardButton(text="У кассы", callback_data='cassa')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
kat.add(k1,k2,k3,k4,k5,k6,k7,k8,back)
###
news=InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Переходи', url=URL_news)
    ]
])
###
connect=InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Написать', url=URL_news)
    ]
])
# А теперь клавиатуры со ссылками на товары
pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url=URL_APPLES)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url=URL_PEAR)
    ]
])

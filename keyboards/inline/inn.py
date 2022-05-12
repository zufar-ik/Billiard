from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db

prod = db.View_prod()

stol_all = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Стол 1', callback_data='Стол 1'),
         InlineKeyboardButton(text='Стол 2', callback_data='Стол 2')],
        [InlineKeyboardButton(text='Стол 3', callback_data='Стол 3'),
         InlineKeyboardButton(text='Стол 4', callback_data='Стол 4')],
        [InlineKeyboardButton(text='Назад', callback_data='back88')]
    ]
)

yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Открыть счёт', callback_data='opens')],
        [InlineKeyboardButton(text='Назад', callback_data='back10')]
    ]
)

cat = db.View_cat()

category = InlineKeyboardMarkup(row_width=2)
for cats in cat:
    category.insert(InlineKeyboardButton(text=f'{cats[1]}', callback_data=f'{cats[0]}'))

category1 = InlineKeyboardMarkup(row_width=2)
category1.insert(InlineKeyboardButton(text='❌Закрыть стол❌', callback_data='clos'))
category1.insert(InlineKeyboardButton(text='🧨Удалить продукты!🧨', callback_data='delete_prod'))
for cats in cat:
    category1.insert(InlineKeyboardButton(text=f'{cats[1]}', callback_data=f'{cats[0]}'))
category1.insert(InlineKeyboardButton(text="Назад", callback_data='main22'))




cate = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Столы', callback_data='stol')],
        [InlineKeyboardButton(text='Бар', callback_data='bar')],
        [InlineKeyboardButton(text='Активные столы', callback_data='active')]
    ]
)



count2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='+1', callback_data='1'), InlineKeyboardButton(text='+2', callback_data='2'),
         InlineKeyboardButton(text='+3', callback_data='3')],
        [InlineKeyboardButton(text='+4', callback_data='4'), InlineKeyboardButton(text='+5', callback_data='5'),
         InlineKeyboardButton(text='+6', callback_data='6')],
        [InlineKeyboardButton(text='+7', callback_data='7'), InlineKeyboardButton(text='+8', callback_data='8'),
         InlineKeyboardButton(text='+9', callback_data='9')],
        [InlineKeyboardButton(text='Отмена', callback_data='otmena')]
    ]
)

category10 = InlineKeyboardMarkup(row_width=2)
for i in cat:
    category10.insert(InlineKeyboardButton(text=f'{i[1]}', callback_data=f'{i[0]}?'))
category10.insert(InlineKeyboardButton(text='Назад', callback_data='back100'))
category10.insert(InlineKeyboardButton(text='Отправить отчет!',callback_data='send_doc'))



from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from data.config import CHANNELS
from keyboards.inline.inn import cate, stol_all, yes_no, category1, count2, category10
from loader import db
from loader import dp
from states.state import Stol, Cart, Peredacha, Prosto, Card_Bar
from xlsxwriter.workbook import Workbook
import os

prod = db.View_prod()
cat = db.View_cat()


@dp.callback_query_handler(text='stol', state='*')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Выберите стол!', reply_markup=stol_all)
    await Stol.start.set()


@dp.callback_query_handler(text='qwerty', state='*')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Выберите продукт!', reply_markup=category10)


@dp.callback_query_handler(text='bar', state='*')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Выберите категорию', reply_markup=category10)

    await Prosto.one.set()


@dp.callback_query_handler(text='back100', state='*')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(text='Выберите действие!', reply_markup=cate)


@dp.callback_query_handler(text='back88', state='*')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(text='Выберите действие!', reply_markup=cate)


for i in prod:
    @dp.callback_query_handler(text=f'{i[4]}?', state='*')
    async def get_prod(call: types.CallbackQuery):
        products10 = InlineKeyboardMarkup(row_width=2)
        CALL1 = call.data
        print(CALL1.strip('?'))
        for i in db.where_prod(category_id=CALL1.strip('?')):
            products10.insert(InlineKeyboardButton(text=f'{i[1]}', callback_data=f'{i[2]}?'))
        products10.insert(InlineKeyboardButton(text='Назад', callback_data='qwerty'))
        await call.message.edit_text('Выберите продукт', reply_markup=products10)
        await Card_Bar.add.set()

for i in prod:
    @dp.callback_query_handler(text=f'{i[2]}?', state=Card_Bar.add)
    async def get_more(call: types.CallbackQuery, state: FSMContext):
        await call.message.edit_text('Выберите количество', reply_markup=count2)
        b = call.data
        a = b.strip('?')
        await state.update_data(
            {'product_id': a}
        )
        await Card_Bar.add.set()


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


@dp.callback_query_handler(state=Card_Bar.add)
async def add(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    print(product_id)
    stol_id = 99999999999
    NAME = db.where_prod(slug=product_id)
    n = call.data
    if is_number(n) == True:
        for i in NAME:
            db.add_product_bar(bar_id=stol_id, name=i[1], quantity=int(n), price=i[3])
            await call.message.delete()
            await call.answer('Ваш заказ добавлен в корзинку!', show_alert=True)
            await call.message.answer('Выберите категорию', reply_markup=category10)
            await state.finish()
    if n == 'otmena':
        await call.message.edit_text('Выберите категорию', reply_markup=category10)


@dp.callback_query_handler(text='send_doc', state='*')
async def send_doc(call: types.CallbackQuery):
    doc = db.select_all_cart_admin()
    print(doc)
    if doc != []:
        workbook = Workbook(
            f'handlers/users/{datetime.now().strftime("%Y_%m_%d")}.xlsx')  # Файл который надо передать админу
        worksheet = workbook.add_worksheet(name="Отчет в баре")
        for i, row in enumerate(doc):
            for j, value in enumerate(row):
                worksheet.write(i, j, value)
        workbook.close()
        await call.message.delete()
        if os.path.exists(f'handlers/users/{datetime.now().strftime("%Y_%m_%d")}.xlsx'):
            await call.message.answer_document(
                open(f'handlers/users/{datetime.now().strftime("%Y_%m_%d")}.xlsx',
                     'rb'))
            await call.bot.send_document(chat_id=CHANNELS[0],
                                         document=open(f'handlers/users/{datetime.now().strftime("%Y_%m_%d")}.xlsx',
                                                       'rb'))
            os.remove(f'handlers/users/{datetime.now().strftime("%Y_%m_%d")}.xlsx')
        db.delete_cart2()
        await call.message.answer("Все данные сохранены в файле", reply_markup=cate)
    else:
        await call.message.edit_text('В базе ничего нет!', reply_markup=cate)


@dp.callback_query_handler(text='back', state='*')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(text='Выберите действие!', reply_markup=cate)


@dp.callback_query_handler(text='back10', state='*')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(text='Выберите действие!', reply_markup=stol_all)
    await Stol.start.set()


@dp.callback_query_handler(text='Стол 1', state=Stol.start)
async def stol1(call: types.CallbackQuery, state: FSMContext):
    title1 = call.data
    await state.update_data(
        {'title': title1}
    )

    await call.message.edit_text('Выберите действие!', reply_markup=yes_no)
    await Stol.down.set()


@dp.callback_query_handler(text='Стол 2', state=Stol.start)
async def stol1(call: types.CallbackQuery, state: FSMContext):
    title1 = call.data
    await state.update_data(
        {'title': title1}
    )

    await call.message.edit_text('Выберите действие!', reply_markup=yes_no)
    await Stol.down.set()


@dp.callback_query_handler(text='Стол 3', state=Stol.start)
async def stol1(call: types.CallbackQuery, state: FSMContext):
    title1 = call.data
    await state.update_data(
        {'title': title1}
    )

    await call.message.edit_text('Выберите действие!', reply_markup=yes_no)
    await Stol.down.set()


@dp.callback_query_handler(text='Стол 4', state=Stol.start)
async def stol1(call: types.CallbackQuery, state: FSMContext):
    title1 = call.data
    await state.update_data(
        {'title': title1}
    )

    await call.message.edit_text('Выберите действие!', reply_markup=yes_no)
    await Stol.down.set()


@dp.callback_query_handler(text='back5', state='*')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(text='Выберите действие!', reply_markup=stol_all)
    await Stol.start.set()


@dp.callback_query_handler(text='opens', state=Stol.down)
async def open_stol(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    title1 = data.get('title')
    data1 = db.time_where(name=title1, active=True)
    try:
        active = (data1[0][5])
        if active != 1:
            if title1 != 'bar':
                a = db.time_start(start=datetime.now().strftime('%Y-%m-%d %H:%M'), name=title1, active=True)
                await state.update_data(
                    {'time_stol': a}
                )
                b = db.time_where(nachalo=datetime.now().strftime('%Y-%m-%d %H:%M'), name=title1, active=True)
                stol_id = b[0][0]

                await state.update_data(
                    {"stol_id": stol_id}
                )
                close = InlineKeyboardMarkup(row_width=1)
                close.insert(InlineKeyboardButton(text='❌Закрыть стол❌', callback_data='close'))
                close.insert(InlineKeyboardButton(text="Назад", callback_data='main'))
                await call.message.edit_text(f'{title1}, Счет открыт в {datetime.now().strftime("%Y-%m-%d %H:%M")}',
                                             reply_markup=close)

                await call.answer(f'{title1}, Счет открыт в {datetime.now().strftime("%Y-%m-%d %H:%M")}',
                                  show_alert=True)
                await Stol.down.set()
        else:
            await call.answer('Этот стол занят!', show_alert=True)
    except IndexError:
        if title1 != 'bar':
            a = db.time_start(start=datetime.now().strftime('%Y-%m-%d %H:%M'), name=title1, active=True)
            await state.update_data(
                {'time_stol': a}
            )
            b = db.time_where(nachalo=datetime.now().strftime('%Y-%m-%d %H:%M'), name=title1, active=True)
            stol_id = b[0][0]

            await state.update_data(
                {"stol_id": stol_id}
            )
            close = InlineKeyboardMarkup(row_width=1)
            close.insert(InlineKeyboardButton(text='❌Закрыть стол❌', callback_data='close'))
            close.insert(InlineKeyboardButton(text="Назад", callback_data='main'))
            await call.message.edit_text(f'{title1}, Счет открыт в {datetime.now().strftime("%Y-%m-%d %H:%M")}',
                                         reply_markup=close)

            await call.answer(f'{title1}, Счет открыт в {datetime.now().strftime("%Y-%m-%d %H:%M")}', show_alert=True)
            await Stol.down.set()


@dp.callback_query_handler(text='close', state='*')
async def back(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    stol_id = data.get('stol_id')
    db.time_end(end=datetime.now().strftime('%Y-%m-%d %H:%M'), id=stol_id)
    price = db.time_where(id=stol_id)
    for i in price:
        a = datetime.strptime((i[1]), "%Y-%m-%d %H:%M")
        b = datetime.strptime((i[2]), "%Y-%m-%d %H:%M")
        minutes = (b - a).total_seconds() / 60
        price = ((b - a).total_seconds() / 60) * 400
        name = i[3]
        db.add_price(price=price, id=stol_id)
        db.add_action(action=False, id=stol_id)
        await call.message.answer(f'{name}:\n'
                                  f'{i[1]} - {i[2]} = {int(price)} сум\n'
                                  f'Вы играли: {minutes} мин.')
        await call.message.bot.send_message(chat_id=CHANNELS[0],
                                            text=f'{i[1]} - {i[2]} = {int(price)} сум\n'f'Вы играли: {int(minutes)} мин.\n')
    await call.message.answer(text='Стол закрыт!', reply_markup=cate)
    await state.finish()


@dp.callback_query_handler(text='active', state='*')
async def menu(call: types.CallbackQuery,state:FSMContext):
    stol_stop = InlineKeyboardMarkup(row_width=1)
    stol_stop.insert(InlineKeyboardButton(text='Назад', callback_data='back'))
    timew = db.select_time()
    for i in timew:
        if i[2] == None:
            stol_stop.insert(InlineKeyboardButton(text=f'{i[3]}', callback_data=f'{i[0]}'))
            await call.message.edit_text('Выберите стол!', reply_markup=stol_stop)
            await Cart.add.set()

            @dp.callback_query_handler(text=f'{i[0]}', state='*')
            async def pre_end(call: types.CallbackQuery, state: FSMContext):
                stol_id = call.data
                await state.update_data(
                    {'stol_id': stol_id}
                )
                await call.message.edit_text('Выберите действие!', reply_markup=category1)
                await Peredacha.per.set()
        await Peredacha.per.set()


timew = db.select_time()


@dp.callback_query_handler(text=f'clos', state='*')
async def end_add(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    call1 = data.get('stol_id')
    print(call1)
    db.time_end(end=datetime.now().strftime('%Y-%m-%d %H:%M'), id=call1)
    price = db.time_where(id=call1)

    for i in price:
        a = datetime.strptime((i[1]), "%Y-%m-%d %H:%M")
        b = datetime.strptime((i[2]), "%Y-%m-%d %H:%M")
        minutes = (b - a).total_seconds() / 60
        price = ((b - a).total_seconds() / 60) * 400
        name = i[3]
        db.add_price(price=price, id=call1)
        db.add_action(action=False, id=call1)
        cart = db.get_products(tg_id=call1)
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        msg = 'Дополнительные заказы:\n\n'
        if len(cart) != 0:
            total = 0
            for product in cart:
                markup.add(f"❌ {product[2]} ❌")
                narx = (int(product[3]) * int(product[4]))
                total += narx
                msg += f"{product[2]}:{product[4]} x {product[3]} = {narx} сум\n\n -------------------------------------\n"
            msg += f"\nОбщая сумма: {int(total) + int(price)} сум\n"
            await call.message.answer(f'{name}:\n'
                                      f'{i[1]} - {i[2]} = {int(price)} сум\n'
                                      f'Вы играли: {minutes} мин.\n'
                                      f'{msg}')

            await call.message.bot.send_message(chat_id=CHANNELS[0],
                                                text=f'{name}:\n{i[1]} - {i[2]} = {int(price)} сум\n'f'Вы играли: {int(minutes)} мин.\n'
                                                     f'{msg}')
            await call.answer(text='Стол закрыт!', show_alert=True)
            await call.message.answer('Выберите действие!', reply_markup=cate)
            db.clear_cart(tg_id=call1)
        else:
            await call.message.answer(f'{name}:\n'
                                      f'{i[1]} - {i[2]} = {int(price)} сум\n'
                                      f'Вы играли: {minutes} мин.\n'
                                      f'{msg}Не было!')
            await call.message.bot.send_message(chat_id=CHANNELS[0],
                                                text=f'{name}:\n{i[1]} - {i[2]} = {int(price)} сум\n'f'Вы играли: {int(minutes)} мин.\n'
                                                     f'{msg}Не было')
            db.clear_cart(tg_id=call1)


pd = db.select_time()
for i in pd:
    @dp.callback_query_handler(text=f'{i[3]}')
    async def delete(call: types.CallbackQuery):
        delet_prod = ReplyKeyboardMarkup(resize_keyboard=True)
        delet_prod.add(KeyboardButton(f'{i[3]}'))
        await call.message.answer('Хотите удалить добавленный продукт?', reply_markup=delet_prod)

for i in prod:
    @dp.callback_query_handler(text=f'{i[4]}', state='*')
    async def get_prod(call: types.CallbackQuery):
        products = InlineKeyboardMarkup(row_width=2)
        CALL1 = call.data
        for i in db.where_prod(category_id=CALL1):
            products.insert(InlineKeyboardButton(text=f'{i[1]}', callback_data=i[2]))
        products.insert(InlineKeyboardButton(text='Назад', callback_data='назад'))
        await call.message.edit_text('Выберите продукт', reply_markup=products)
        await Cart.add.set()


@dp.callback_query_handler(text='назад', state='*')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(text='Выберите действие!', reply_markup=category1)
    await Stol.down.set()


for i in prod:
    @dp.callback_query_handler(text=f'{i[2]}', state='*')
    async def get_more(call: types.CallbackQuery, state: FSMContext):
        await call.message.edit_text('Выберите количество', reply_markup=count2)
        a = call.data
        await state.update_data(
            {'product_id': a}
        )
        await Cart.add.set()


@dp.callback_query_handler(state=Cart.add)
async def add(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    stol_id = data.get('stol_id')
    NAME = db.where_prod(slug=product_id)
    n = call.data
    if is_number(n) == True:
        for i in NAME:
            product = db.check_product(tg_id=stol_id, name=i[1])
            if product:
                db.update_product(tg_id=stol_id, name=i[1], quantity=int(product[3]) + int(n), price=i[3])
            else:
                db.add_product(tg_id=stol_id, name=i[1], quantity=int(n), price=i[3])
            await call.message.delete()
            await call.answer('Ваш заказ добавлен в корзинку!', show_alert=True)
            await call.message.answer('Выберите категорию', reply_markup=category1)
            await Stol.down.set()
    elif n == 'otmena':
        await call.message.delete()
        await call.message.answer('Выберите категорию', reply_markup=cate)
    elif n == 'main22':
        await call.message.delete()
        await call.message.answer('Выберите категорию', reply_markup=cate)
        await Peredacha.per.set()
    else:
        await call.answer(text='Нажмите "НАЗАД"')
    await Cart.add.set()


@dp.callback_query_handler(text='main', state='*')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Выберите стол!', reply_markup=cate)


@dp.callback_query_handler(text='main22', state='*')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Выберите действие!', reply_markup=cate)


@dp.callback_query_handler(text='delete_prod', state='*')
async def menu(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    stol_id = data.get('stol_id')
    product_all = db.get_products(tg_id=stol_id)
    del_prod = InlineKeyboardMarkup(row_width=2)
    for i in product_all:
        del_prod.insert(InlineKeyboardButton(text=f'{i[2]}', callback_data=f'{i[0]}'))
    del_prod.insert(InlineKeyboardButton(text='Назад', callback_data='mack'))
    await call.message.edit_text('Выберите продукт которого хотите удалить!', reply_markup=del_prod)
    for i in product_all:
        @dp.callback_query_handler(text=f'{i[0]}', state='*')
        async def delet_select(call: types.CallbackQuery):
            call1 = call.data
            print(call1)
            print(stol_id)
            db.delete_product(tg_id=stol_id, id=f'{call1}')
            await call.message.edit_text(f'Удален из стола!', reply_markup=category1)


@dp.callback_query_handler(text='mack', state='*')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Выберите продукт которого хотите удалить!', reply_markup=category1)

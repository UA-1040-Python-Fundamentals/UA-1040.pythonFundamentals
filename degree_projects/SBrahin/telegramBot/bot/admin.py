import json
import string

from aiogram import F, Router, types, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram import flags
from aiogram.fsm.context import FSMContext
import utils
from states import Gen

import kb
import text


router = Router()

#Старт бота та привітання
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
#Вихід з розділу в загальне меню
@router.message(F.text == "Меню")
@router.message(F.text == "Вийти в меню")
@router.message(F.text == "◀️ Вийти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)
#Генерування тексту
@router.callback_query(F.data == "generate_text")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.text_prompt)
    await clbck.message.edit_text(text.gen_text)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.exit_kb)

@router.message(Gen.text_prompt)
@flags.chat_action("typing")
async def generate_text(msg: Message):
    prompt = msg.text
    mesg = await msg.answer(text.gen_wait)
    res = await utils.generate_text(prompt)
    if not res:
        return await mesg.edit_text(text.gen_error, reply_markup=kb.iexit_kb)
    await mesg.edit_text(res[0] + text.text_watermark, disable_web_page_preview=True)
#Генерування зображення
@router.callback_query(F.data == "generate_image")
async def input_image_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.img_prompt)
    await clbck.message.edit_text(text.gen_image)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.exit_kb)

@router.message(Gen.img_prompt)
@flags.chat_action("upload_photo")
async def generate_image(msg: Message):
    prompt = msg.text
    mesg = await msg.answer(text.gen_wait)
    img_res = await utils.generate_image(prompt)
    if len(img_res) == 0:
        return await mesg.edit_text(text.gen_error, reply_markup=kb.iexit_kb)
    await mesg.delete()
    await mesg.answer_photo(photo=img_res[0], caption=text.img_watermark)

#Генерування оплати
@router.callback_query(F.data == "buy_tokens")
async def input_text_prompt(clbck: CallbackQuery):
    await clbck.message.answer_invoice(
        #chat_id=message.chat.id,
        title='Донат для розвитку нашої спільноти',
        description='Ваші донати, спонукають нас робити світ краще',
        payload='Payment through a bot',
        provider_token='410694247:TEST:296110f2-5788-4755-ad89-57831f43bfe1',
        currency='uah',
        prices=[
            LabeledPrice(
                label='Мінімальна сумма донату',
                amount= 1000
            )
        ],
        max_tip_amount=100000,
        suggested_tip_amounts=[5000, 10000, 50000, 100000],
        start_parameter='',
        provider_data=None,
        photo_url='https://cdn.create.vista.com/api/media/medium/398454150/stock-photo-cropped-view-woman-putting-coin-penny-jar-donate-lettering-wooden?token=',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,#######################################
        request_timeout=15
    )

#Функція для підтвердження оплати з нашого боку
@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)

#Повідомлення після оплати
@router.message(F.content_type==types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await message.delete()
    msg=f'🥳 Дякуємо за ваш донат {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'\
        f'\r \nВашу допомогу не оцінити😇'
    await message.answer(msg)
    await message.answer(text.gen_exit, reply_markup=kb.exit_kb )

#Генерування допомоги
@router.callback_query(F.data == "help")
async def input_text_prompt(clbck: CallbackQuery):
    await clbck.message.answer(text.help_t)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.exit_kb)


#Фільтр мату
@router.message()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans("",'',string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('censor.json')))) != set():
        await message.reply('Спілкуйтесь ввічливо!')
        await message.delete()

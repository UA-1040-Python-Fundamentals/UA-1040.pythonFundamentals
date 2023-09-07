from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝 Згенерувати текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Згенерувати зображення", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Зробити донат", callback_data="buy_tokens"),
    InlineKeyboardButton(text="📲 Перейти до нашого каналу", callback_data="balance", url='https://t.me/Smartixxxxxx')],
    [InlineKeyboardButton(text="🔎 Допомога", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Вийти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Вийти в меню", callback_data="menu")]])



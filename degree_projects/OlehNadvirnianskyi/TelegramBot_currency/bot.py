import telebot
from binance.client import Client
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot("BOT TOKEN")
api_key = 'CREYPTO key'
api_secret = 'API crypto key'

currency_btn = CurrencyConverter()
client = Client(api_key, api_secret)
amount = 0
currency_type = ''
pair = ''


@bot.message_handler(commands=['start'])
def start(message):
    """ This function greets the user and offers to choose the type of exchange after launching the bot """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    currency_btn = types.KeyboardButton("💵Currency💵")
    crypto_btn = types.KeyboardButton("📈Crypro-Currency📈")
    markup.add(currency_btn, crypto_btn)
    msg = bot.send_message(message.chat.id, "👋🏻Hi!👋🏻\n😊Welcome to exchangeBOT😊\n💵Choose the type of exchange💵:",
                           reply_markup=markup)
    bot.register_next_step_handler(msg, select_pair)


def select_pair(message):
    ''' This function offers to enter a currency or cryptocurrency pair based on the user's previous choice '''
    global currency_type
    currency_type = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn = types.KeyboardButton("👈🏼Back")
    markup.add(back_btn)

    if currency_type == "💵Currency💵":
        bot_message_cur = bot.send_message(message.chat.id, "💵Enter the currency pair in format [USD/EUR]💵:",
                                           reply_markup=markup)
        bot.register_next_step_handler(bot_message_cur, pick_pair)
    elif currency_type == "📈Crypro-Currency📈":
        bot_message_crypto = bot.send_message(message.chat.id,
                                              "📈Enter the crypto-currency pair in format [BTC/USDT]📈, "
                                              "\n❗️❗️But be careful and change only the FIRST variable❗️❗️:",
                                              reply_markup=markup)
        bot.register_next_step_handler(bot_message_crypto, pick_pair)
    else:
        msg = bot.send_message(message.chat.id, "😱Wrong input,try again.😱")
        bot.register_next_step_handler(msg, select_pair)


def pick_pair(message):
    ''' This function offers the user to enter the amount of currency to exchange '''
    global pair
    pair = message.text
    msg = bot.send_message(message.chat.id, f"😎Your pair is {pair}.😎\n💵Enter the amount of currency:💵")
    bot.register_next_step_handler(msg, select_amount)


def select_amount(message):
    ''' This function accepts the value of the amount of currency and checks it for an acceptable input format,
     and then, depending on the type of exchange, runs the next function '''
    global amount, currency_type
    try:
        amount = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "😱Wrong value, try again!😱")
        bot.register_next_step_handler(message, select_amount)
        return

    if amount <= 0:
        bot.send_message(message.chat.id, "😱Value is too small, try again!😱")
        bot.register_next_step_handler(message, select_amount)
    else:
        if currency_type == "💵Currency💵":
            convert_currency(message)
        else:
            convert_crypto(message)


def convert_currency(message):
    """This function converts the currency and returns a message with the result"""
    global pair, amount
    if message.text == "👈🏼Back":
        back_msg = bot.send_message(message.chat.id, "Ok, try again:)")
        bot.register_next_step_handler(back_msg, pick_pair)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        again_btn = types.KeyboardButton("🔁Again🔁")
        markup.add(again_btn)
        input_pair = str(pair)
        pair = input_pair.split('/')
        pair1 = pair[0]
        pair2 = pair[1]
        res = currency_btn.convert(amount, pair[0], pair[1])
        result_msg = bot.send_message(message.chat.id, f"💹Result: {amount} {pair1} = {res} {pair2}.💹",
                                      reply_markup=markup)
        bot.register_next_step_handler(result_msg, start)


def convert_crypto(message):
    """this function converts the crypto-currency and returns a message with the result"""
    global pair, amount
    if message.text == "👈🏼Back":
        back_msg = bot.send_message(message.chat.id, "Ok, try again:)")
        bot.register_next_step_handler(back_msg, pick_pair)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        again_btn = types.KeyboardButton("🔁Again🔁")
        markup.add(again_btn)
        pair = str(pair)
        pair_for_res = pair.split('/')
        pair_for_calc = ''.join(pair_for_res)
        pair1 = pair_for_res[0]
        pair2 = pair_for_res[1]
        ticker = client.get_ticker(symbol=pair_for_calc)
        crypto_price = ticker['lastPrice']
        res = amount / float(crypto_price)
        result_msg = bot.send_message(message.chat.id, f"💹Result: {amount} {pair2} = {res} {pair1}.💹",
                                      reply_markup=markup)
        bot.register_next_step_handler(result_msg, start)


if __name__ == "__main__":
    bot.polling()

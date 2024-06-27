from auth_data import token
import requests
from datetime import datetime
import telebot
from telebot import types
def crypto_bahalar(crypto):
    url=f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    jogaby=requests.get(url)
    data=jogaby.json()
    shu_gun_sene = datetime.now().strftime("%d.%m.%Y %H:%M")
    if crypto in data and "usd" in data[crypto]:
         return data[crypto]["usd"]
    else:
         return"Bagyshlan kripto bahasyny owrenip bilmedim"
bitcoin_bahasy=crypto_bahalar("bitcoin")
print(f"Bitcoinin bahasy:{bitcoin_bahasy}$")
menin_botym=telebot.TeleBot(token)
@menin_botym.message_handler(commands=["start"])
def start_knopka(message):
     if message:
          klawiatura=types.InlineKeyboardMarkup(row_width=2)
          bitcoin_knopka=types.InlineKeyboardButton("Bitcoin bahasy",callback_data="bitcoin")
          litecoin_knopka=types.InlineKeyboardButton("Litecoin bahasy",callback_data="litecoin")
          etherem_knopka=types.InlineKeyboardButton("Etherem bahasy",callback_data="ethereum")
          klawiatura.add(bitcoin_knopka,litecoin_knopka,etherem_knopka)
          menin_botym.send_message(message.chat.id,"Haýsy kripto-walyutanyn bahasny owrensiniz gelyar?",reply_markup=klawiatura)
@menin_botym.callback_query_handler(func=lambda call:True)
def knopkalara_basylanda_jogap(callback):
    if callback.massage:
        bahasy=crypto_bahalar(callback.data)
        menin_botym.send_message(callback.massage.chat.id,f"{bahasy}")
        start_knopka(callback.message)
menin_botym.polling()



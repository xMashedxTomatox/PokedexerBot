from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import json
import re


def main():
    updater = Updater("your telegram bot key")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('search',search))
    updater.start_polling()
    updater.idle()

def search(update, context):
    term = context.args[0]
    contents = pokedex(term)
    pic = contents["sprites"]["other"]["official-artwork"]["front_default"]
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id,photo=pic)
    context.bot.send_message(chat_id=chat_id,text=description(contents))
    


def pokedex(term):
    contents = requests.get('https://pokeapi.co/api/v2/pokemon/' + term)
    return contents.json()

def description(pokemon):
    types = "Type(s): "
    for x in pokemon["types"]:
        types = types + x["type"]["name"] + " "
    abilities = "Abilitie(s): "
    for x in pokemon["abilities"]:
        abilities = abilities + x["ability"]["name"] + " "
    baseStats = "Base Stats:" + "\n"
    for x in pokemon["stats"]:
        baseStats = baseStats + x["stat"]["name"] + ": " + str(x["base_stat"]) + "\n"
    return types + "\n" + abilities + "\n" + baseStats
    
        




if __name__ == '__main__':
    main()

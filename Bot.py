import logging
import json

from telegram import *
from telegram.ext import *

myData = {}
with open('userData.json') as json_file:
	data = json.load(json_file)
	for p in data['users']:
		myData[p["username"]] = p["id"]
  
def start(bot,update):
	
	kb = [[KeyboardButton('/Diego',request_location=True),KeyboardButton('/Victor',request_location=True)],
	   		[KeyboardButton('/Pepin',request_location=True)]]
	kb_markup = ReplyKeyboardMarkup(kb)
	bot.send_message(chat_id=update.message.chat_id,
					 text="Elige acción",
					 reply_markup=kb_markup)
 
def warnVictor(bot,update):
	user = update.message.from_user
	warnUser(user,"Victor",372206266,bot,update)

	
def warnDiego(bot,update):
	print(update.message.location)
	user = update.message.from_user
	warnUser(user,"Diego",223472488,bot,update)

		  
def warnUser(user,name,chat_id,bot,update):
	if user['id'] == myData['Peples']:
		bot.send_message(chat_id=chat_id,text="SAL DE CASA WEY")
		update.message.reply_text(name + " avisado")

def location(bot, update):
	message = None
	if update.edited_message:
		message = update.edited_message
	else:
		message = update.message
	current_pos = (message.location.latitude, message.location.longitude)
	update.message.reply_text("https://www.google.es/maps/@"+str(message.location.latitude)+","+str(message.location.longitude)+",7z")

	print("https://www.google.es/maps/@"+str(message.location.latitude)+","+str(message.location.longitude)+",18z")

def main():
	updater = Updater('1031182043:AAF66tKjzE1wZl1HdzyOVca1ec7fEARwZqg')
	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('victor', warnVictor))
	updater.dispatcher.add_handler(CommandHandler('diego', warnDiego))
	location_handler = MessageHandler(Filters.location, location)
	updater.dispatcher.add_handler(location_handler)

	updater.start_polling()
	updater.idle

if __name__ == '__main__':
	main()

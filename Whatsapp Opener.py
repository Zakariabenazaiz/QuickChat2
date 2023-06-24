import telegram
from telegram.ext import Updater, MessageHandler, Filters
import urllib.parse

TOKEN = '6133105355:AAFAe6GVOVJexlzv9gz7CEBHyTyEJd5g5Ec'

def start(update, context):
    welcome_message = "Welcome to the Quick Chat bot! Please enter a phone number with the international code."
    update.message.reply_text(welcome_message)

def handle_phone_number(update, context):
    phone_number = update.message.text
    formatted_number = urllib.parse.quote(phone_number, safe='')
    formatted_number = formatted_number.replace(' ', '')  # Remove any spaces in the phone number
    whatsapp_url = f"https://api.whatsapp.com/send?phone={formatted_number}&text=?"
    update.message.reply_text(f"Click the link below to open the chat in WhatsApp:\n\n{whatsapp_url}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_phone_number))
    dp.add_handler(MessageHandler(Filters.command, start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

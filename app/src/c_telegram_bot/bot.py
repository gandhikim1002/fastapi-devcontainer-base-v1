from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# TOKEN = "YOUR_TELEGRAM_BOT_API_TOKEN"
TOKEN = "8210690679:AAG4H-qyd8GGc8sBu1528Qvp58sUJ0QwF5E"

bot = Bot(TOKEN)
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Welcome to the FastAPI Chatbot.')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Send /start to start the bot.')

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help_command)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
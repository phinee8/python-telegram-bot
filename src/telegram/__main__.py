```python
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "6251031144:AAFG7VEvwlONa89Xp-nFjInIUWmP8PXBIQE"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bonjour! Je suis ton bot. Comment puis-je t'aider?")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Voici les commandes disponibles:\n/start - démarrer le bot\n/help - aide")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if _name_ == "_main_":
    main()
```

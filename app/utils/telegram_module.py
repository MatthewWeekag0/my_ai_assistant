# app/telegram_module.py

from telegram.ext import Updater, MessageHandler, Filters

class TelegramModule:
    def __init__(self, token, router):
        self.updater = Updater(token=token)
        self.router = router
        dp = self.updater.dispatcher
        dp.add_handler(MessageHandler(Filters.text | Filters.photo | Filters.video, self.handle))

    def start(self):
        self.updater.start_polling()

    def handle(self, update, context):
        text = update.message.text or "<media>"
        response = self.router.handle_request(text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

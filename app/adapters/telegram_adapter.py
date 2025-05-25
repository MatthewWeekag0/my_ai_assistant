# app/adapters/telegram_adapter.py
from telegram.ext import Updater, MessageHandler, Filters
from typing import Any

class TelegramModule:
    """
    Телеграм-бот: принимает текст и пересылает ответ от Router.
    """

    def __init__(self, token: str, router: Any) -> None:
        self.router = router
        self.updater = Updater(token=token, use_context=True)
        dp = self.updater.dispatcher
        dp.add_handler(MessageHandler(Filters.text, self._handle))

    def start(self) -> None:
        """Запускает бота."""
        self.updater.start_polling()

    def _handle(self, update, context) -> None:
        text = update.message.text or ""
        response = self.router.handle_request(text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

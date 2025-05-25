# app/adapters/telegram_adapter.py
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, MessageHandler,
    ContextTypes, filters
)
from typing import Any
from app.core.config import Config

class TelegramAdapter:
    """Адаптер для Telegram Bot API (читает BOT_TOKEN из config.ini)."""

    def __init__(self, router: Any, config_path: str = 'config.ini') -> None:
        cfg = Config(config_path)
        token = cfg.get('TELEGRAM', 'BOT_TOKEN')
        if not token:
            raise ValueError("В config.ini не указан TELEGRAM:BOT_TOKEN")

        self.router = router
        self.app = ApplicationBuilder().token(token).build()
        self.app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle)
        )

    async def _handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            user_text = update.message.text
            response = self.router.handle_request(user_text)
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=response
            )
        except Exception as e:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Ошибка бота: {e}"
            )

    def start(self) -> None:
        self.app.run_polling()
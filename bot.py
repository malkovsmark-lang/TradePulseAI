from dotenv import load_dotenv
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBAPP_URL = "https://example.com"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            text="📈 Открыть TradePulseAI",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]

    await update.message.reply_text(
        "Добро пожаловать в TradePulseAI",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("TradePulseAI запущен...")

    app.run_polling()


if __name__ == "__main__":
    main()
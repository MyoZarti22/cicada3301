"""
Telegram Bot for Stage 6 - Cicada 3301-style Transmission
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sends one message in a cold, cryptic "we are testing you" register:
7 season.episode.word coordinates, then asks her to find what they're
about and the single word that connects them.

SETUP (takes 5 minutes):
1. Open Telegram → search @BotFather
2. Send: /newbot
3. Give it a name (e.g. "The Signal") and a username (e.g. signalbot_xxx)
4. BotFather gives you a TOKEN — paste it below where it says YOUR_TOKEN_HERE
5. Install dependencies: pip install python-telegram-bot
6. Run this file: python3 telegram_bot.py
7. Your bot is live. Put the @username in stage6.html.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ── PASTE YOUR BOT TOKEN HERE ──────────────────────────────────────────────────
BOT_TOKEN = "8759870497:AAE3NaY0HohTRukG-mqnQxQUb2zSebEuxyI"
# ──────────────────────────────────────────────────────────────────────────────


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Single message — Cicada 3301-styled transmission
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Hello.\n\n"
            "We have been watching.\n"
            "You have been chosen.\n\n"
            "Seven fragments remain, scattered across a story you already know.\n\n"
            "01.01.01\n"
            "02.01.01\n"
            "03.01.01\n"
            "04.01.01\n"
            "05.01.01\n"
            "06.01.01\n"
            "07.01.01\n\n"
            "Find out what it's about.\n\n"
            "When the fragments are recovered, a single word will remain.\n\n"
            "What single word connects all recovered clues?\n\n"
        )
    )


def main():
    print("Bot is running... Press Ctrl+C to stop.")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()

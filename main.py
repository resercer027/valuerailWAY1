import os
import asyncio
import schedule
import time
import threading
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)
from auto_sender import run_combined_scrapers

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = None
app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CHAT_ID
    CHAT_ID = update.effective_chat.id
    await update.message.reply_text("Bot attivo! Ti invierò scommesse value ogni 10 minuti.")

async def valuebet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bets = run_combined_scrapers()
    if bets:
        for bet in bets:
            await update.message.reply_text(bet)
    else:
        await update.message.reply_text("Nessuna value bet valida trovata al momento.")

async def send_auto_value_bets():
    if CHAT_ID:
        bets = run_combined_scrapers()
        for bet in bets:
            await app.bot.send_message(chat_id=CHAT_ID, text=bet)
        if not bets:
            await app.bot.send_message(chat_id=CHAT_ID, text="Nessuna value bet automatica trovata al momento.")

def schedule_loop():
    schedule.every(10).minutes.do(lambda: asyncio.run(send_auto_value_bets()))
    while True:
        schedule.run_pending()
        time.sleep(1)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("valuebet", valuebet))

threading.Thread(target=schedule_loop, daemon=True).start()

if __name__ == '__main__':
    app.run_polling()

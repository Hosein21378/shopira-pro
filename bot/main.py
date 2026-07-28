import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from bot.handlers import start, shop, payment, admin, support

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def error_handler(update: Update, context):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN not found in .env")

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start.start))
    application.add_handler(CallbackQueryHandler(shop.shop_menu, pattern="^shop$"))
    application.add_handler(CallbackQueryHandler(payment.payment_menu, pattern="^payment$"))
    application.add_handler(CallbackQueryHandler(support.support_menu, pattern="^support$"))
    application.add_handler(CallbackQueryHandler(admin.admin_menu, pattern="^admin$"))
    application.add_handler(CallbackQueryHandler(start.start, pattern="^back_main$"))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, support.handle_ai_message))
    application.add_error_handler(error_handler)

    logger.info("✅ Shopira Pro Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()

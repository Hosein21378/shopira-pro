import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def admin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    admin_ids = [int(os.getenv("ADMIN_ID", "0"))]
    if update.effective_user.id not in admin_ids:
        await query.edit_message_text("⛔ شما دسترسی به پنل مدیریت ندارید.")
        return

    keyboard = [
        [InlineKeyboardButton("📊 آمار فروش", callback_data="admin_stats")],
        [InlineKeyboardButton("👥 مدیریت کاربران", callback_data="admin_users")],
        [InlineKeyboardButton("🛍️ مدیریت محصولات", callback_data="admin_products")],
        [InlineKeyboardButton("🔙 بازگشت", callback_data="back_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = "⚙️ **پنل مدیریت Shopira Pro**"

    await query.edit_message_text(text, reply_markup=reply_markup)

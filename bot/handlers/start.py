from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("🛍️ فروشگاه", callback_data="shop")],
        [InlineKeyboardButton("💳 پرداخت و موجودی", callback_data="payment")],
        [InlineKeyboardButton("🤖 پشتیبانی هوشمند", callback_data="support")],
        [InlineKeyboardButton("⚙️ پنل مدیریت", callback_data="admin")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = f"""
سلام {user.first_name} عزیز! 👋

به **Shopira Pro** خوش آمدید.

ربات فروشگاهی مدرن و حرفه‌ای با:
• فروشگاه هوشمند
• پرداخت آنلاین پاسارگاد
• پشتیبانی هوش مصنوعی
• مینی‌اپ پیشرفته

لطفاً یکی از گزینه‌ها را انتخاب کنید:
"""

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def shop_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("📱 اشتراک VPN ماهانه", callback_data="buy_vpn_1m")],
        [InlineKeyboardButton("📱 اشتراک VPN سه‌ماهه", callback_data="buy_vpn_3m")],
        [InlineKeyboardButton("📱 اشتراک VPN سالانه", callback_data="buy_vpn_12m")],
        [InlineKeyboardButton("🔙 بازگشت به منو", callback_data="back_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🛍️ **فروشگاه Shopira Pro**

لطفاً پلن مورد نظر خود را انتخاب کنید:

• **ماهانه**: ۱۵۰,۰۰۰ تومان
• **سه‌ماهه**: ۴۰۰,۰۰۰ تومان
• **سالانه**: ۱,۴۰۰,۰۰۰ تومان

(قیمت‌ها قابل تغییر هستند)
"""

    await query.edit_message_text(text, reply_markup=reply_markup)

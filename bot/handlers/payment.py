from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.pasargad import PasargadPayment
import uuid
from datetime import datetime

async def payment_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("💳 شارژ موجودی با پاسارگاد", callback_data="charge_pasargad")],
        [InlineKeyboardButton("📜 تاریخچه تراکنش‌ها", callback_data="transactions")],
        [InlineKeyboardButton("🔙 بازگشت", callback_data="back_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
💳 **بخش پرداخت و موجودی**

موجودی فعلی شما: **۰ تومان**

برای خرید از فروشگاه یا شارژ موجودی، از گزینه‌های زیر استفاده کنید.
"""

    await query.edit_message_text(text, reply_markup=reply_markup)


async def charge_with_pasargad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # مثال: ایجاد فاکتور
    invoice_number = f"INV-{uuid.uuid4().hex[:8].upper()}"
    invoice_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    pasargad = PasargadPayment()
    
    # در حالت واقعی باید مبلغ را از کاربر بگیریم
    amount = 150000  # تومان

    result = await pasargad.create_payment(
        amount=amount,
        invoice_number=invoice_number,
        invoice_date=invoice_date,
        mobile="09121234567"  # بعداً از دیتابیس
    )

    if result.get("success"):
        payment_url = result.get("redirectUrl")
        keyboard = [[InlineKeyboardButton("🔗 رفتن به درگاه پرداخت", url=payment_url)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"✅ فاکتور #{invoice_number} ایجاد شد.\n\n"
            f"مبلغ: {amount:,} تومان\n\n"
            "لطفاً روی لینک زیر کلیک کنید:",
            reply_markup=reply_markup
        )
    else:
        await query.edit_message_text(
            "❌ خطا در اتصال به درگاه پاسارگاد.\n"
            "لطفاً بعداً تلاش کنید."
        )

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import os
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def support_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = """
🤖 **پشتیبانی هوشمند Shopira Pro**

سلام! من دستیار هوشمند ربات هستم.

هر سوالی در مورد فروشگاه، پرداخت، سرویس‌ها و ... داری بپرس.

(در حال حاضر پاسخ‌ها توسط هوش مصنوعی داده می‌شود)
"""

    await query.edit_message_text(text)


async def handle_ai_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # اگر کاربر در حالت پشتیبانی باشد
    if context.user_data.get("in_support", False):
        try:
            response = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "شما یک دستیار فروشگاهی حرفه‌ای و دوستانه به زبان فارسی هستید."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=300
            )
            answer = response.choices[0].message.content
            await update.message.reply_text(answer)
        except Exception as e:
            await update.message.reply_text("متأسفانه در حال حاضر قادر به پاسخگویی نیستم.")
    else:
        # پیام معمولی
        pass


def enable_ai_support(context):
    context.user_data["in_support"] = True

Workspace



README.md


🛍️ Shopira Pro
ربات فروشگاهی تلگرام فوق‌العاده حرفه‌ای و مدرن‌تر از میرزا پرو

✅ مینی‌اپ مدرن و سریع
✅ اتصال کامل به درگاه پاسارگاد
✅ پشتیبانی هوشمند با هوش مصنوعی
✅ معماری تمیز و مقیاس‌پذیر (Python + FastAPI)
✅ مناسب فروش VPN، اکانت، محصول دیجیتال و ...
✨ ویژگی‌های برتر نسبت به میرزا پرو
ویژگی	میرزا پرو	Shopira Pro
معماری	PHP قدیمی	Python + FastAPI (مدرن)
مینی‌اپ	ساده	کاملاً مدرن + Responsive
پشتیبانی	ساده	AI هوشمند (GPT-like)
درگاه پرداخت	دارد	پاسارگاد بهینه + تست
گزارش‌گیری	پایه	داشبورد زنده + آمار
مقیاس‌پذیری	متوسط	عالی (Redis + PostgreSQL)
کد منبع	نیمه‌بسته	کاملاً اوپن‌سورس و تمیز
🚀 نصب و راه‌اندازی
پیش‌نیازها
Python 3.11+
PostgreSQL (یا SQLite برای شروع)
توکن ربات تلگرام
درگاه پاسارگاد (Merchant Code + Certificate)
گام‌های نصب
Bash

git clone https://github.com/YOUR_USERNAME/shopira-pro.git
cd shopira-pro

python -m venv venv
source venv/bin/activate     # Linux/Mac
# venv\Scripts\activate     # Windows

pip install -r requirements.txt
فایل .env
Bash

cp .env.example .env
سپس مقادیر را در فایل .env وارد کنید.

اجرای ربات
Bash

python -m bot.main
اجرای مینی‌اپ (در حال توسعه)
Bash

uvicorn miniapp.app:app --reload --port 8000
📁 ساختار پروژه
text

shopira-pro/
├── bot/                    # ربات تلگرام
│   ├── handlers/           # هندلرهای مختلف
│   ├── services/           # سرویس‌ها (پاسارگاد، AI، پنل)
│   ├── keyboards/
│   └── states/
├── miniapp/                # مینی‌اپ (وب داخل تلگرام)
├── database/
├── services/
├── utils/
├── .env.example
├── requirements.txt
├── README.md
└── docker-compose.yml
📌 بخش‌های اصلی که باید بسازی
bot/main.py — نقطه ورود ربات
services/pasargad.py — اتصال به درگاه پاسارگاد
bot/handlers/shop.py — بخش فروشگاه
miniapp/ — مینی‌اپ
database/models.py — مدل‌های دیتابیس
🔐 امنیت و نکات مهم
هرگز .env را در گیت هاب آپلود نکنید.
Certificate پاسارگاد را در پوشه امن نگه دارید.
برای محیط production از PostgreSQL + Redis استفاده کنید.
📞 ارتباط و مشارکت
هر سوالی داشتی یا می‌خوای بخشی رو باهم بسازیم، بگو!

نسخه: 1.0.0
تاریخ: ۱۴۰۵/۰۵/۰۶

این پروژه کاملاً از صفر نوشته شده و هدفش ایجاد یک ربات فروشگاهی بهتر از میرزا پرو است.

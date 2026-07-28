# 🚀 راهنمای انتقال Shopira Pro به سرور جدید

## مراحل انتقال کامل (با کمترین downtime)

### ۱. بکاپ گرفتن از سرور فعلی

```bash
# بکاپ دیتابیس
./scripts/backup.sh

# یا بکاپ دستی
docker exec shopira-db pg_dump -U shopira shopira > shopira_backup_$(date +%Y%m%d).sql
```

### ۲. کپی کردن فایل‌ها به سرور جدید

```bash
# روی سرور فعلی
scp -r shopira-pro user@new-server:/home/user/

# یا استفاده از rsync
rsync -avz --progress shopira-pro/ user@new-server:/home/user/shopira-pro/
```

### ۳. روی سرور جدید

```bash
cd /home/user/shopira-pro

# نصب Docker (اگر نصب نیست)
curl -fsSL https://get.docker.com | sh

# اجرای پروژه
docker compose up -d --build
```

### ۴. بازگردانی دیتابیس

```bash
# اگر بکاپ gz دارید
gunzip -c shopira_backup_xxxx.sql.gz | docker exec -i shopira-db psql -U shopira shopira

# یا
./scripts/restore.sh backups/shopira_backup_xxxx.sql.gz
```

### ۵. تنظیمات نهایی

1. توکن ربات و متغیرهای `.env` را به‌روز کنید
2. Certificate پاسارگاد را کپی کنید
3. دامنه را به سرور جدید تغییر دهید
4. ربات را تست کنید

---

## بکاپ خودکار روزانه (پیشنهادی)

اسکریپت `backup.sh` را به cronjob اضافه کنید:

```bash
crontab -e
```

و این خط را اضافه کنید:

```bash
0 3 * * * cd /home/user/shopira-pro && ./scripts/backup.sh
```

---

## نکات مهم

- همیشه قبل از مهاجرت بکاپ بگیرید
- Certificate پاسارگاد را حتماً کپی کنید
- بعد از مهاجرت، توکن ربات را تست کنید
- بکاپ‌ها را در جای امن نگه دارید

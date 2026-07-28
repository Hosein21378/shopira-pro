# 🚀 راهنمای انتقال Shopira Pro به سرور جدید

## مراحل انتقال کامل

### ۱. بکاپ گرفتن از سرور فعلی

```bash
./scripts/backup.sh
```

### ۲. کپی کردن فایل‌ها به سرور جدید

```bash
scp -r shopira-pro user@new-server:/home/user/
```

### ۳. روی سرور جدید

```bash
cd /home/user/shopira-pro
docker compose up -d --build
```

### ۴. بازگردانی دیتابیس

```bash
./scripts/restore.sh backups/shopira_backup_xxxx.sql.gz
```

### ۵. تنظیمات نهایی

- توکن ربات و متغیرهای `.env` را به‌روز کنید
- Certificate پاسارگاد را کپی کنید
- دامنه را به سرور جدید تغییر دهید
```
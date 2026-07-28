# 🛠️ اسکریپت‌های کمکی Shopira Pro

این پوشه شامل اسکریپت‌های کاربردی برای مدیریت، بکاپ و مهاجرت است.

## اسکریپت‌ها

| اسکریپت | توضیح | نحوه استفاده |
|---------|-------|-------------|
| `backup.sh` | بکاپ خودکار دیتابیس | `./scripts/backup.sh` |
| `restore.sh` | بازگردانی دیتابیس | `./scripts/restore.sh backups/xxx.sql.gz` |
| `migrate_to_new_server.md` | راهنمای کامل مهاجرت | مطالعه فایل |

## راه‌اندازی اولیه

```bash
chmod +x scripts/*.sh
```

## بکاپ‌گیری دستی

```bash
./scripts/backup.sh
```

بکاپ‌ها در پوشه `backups/` ذخیره می‌شوند.

## بازگردانی

```bash
./scripts/restore.sh backups/shopira_backup_20250728_143022.sql.gz
```

## مهاجرت به سرور جدید

فایل `migrate_to_new_server.md` را مطالعه کنید.

#!/bin/bash

# =============================================
# Shopira Pro - Database Restore Script
# =============================================

if [ -z "$1" ]; then
    echo "Usage: ./restore.sh <backup_file.sql.gz>"
    echo "Example: ./restore.sh backups/shopira_backup_20250728_143022.sql.gz"
    exit 1
fi

BACKUP_FILE=$1

if [ ! -f "$BACKUP_FILE" ]; then
    echo "❌ Backup file not found: $BACKUP_FILE"
    exit 1
fi

echo "⚠️  WARNING: This will overwrite the current database!"
read -p "Are you sure you want to continue? (y/N): " confirm

if [[ $confirm != [yY] ]]; then
    echo "Cancelled."
    exit 0
fi

echo "🔄 Restoring database from $BACKUP_FILE..."

# استخراج فایل gzip اگر لازم باشد
if [[ $BACKUP_FILE == *.gz ]]; then
    gunzip -c "$BACKUP_FILE" | docker exec -i shopira-db psql -U shopira shopira
else
    docker exec -i shopira-db psql -U shopira shopira < "$BACKUP_FILE"
fi

if [ $? -eq 0 ]; then
    echo "✅ Database restored successfully!"
else
    echo "❌ Restore failed!"
    exit 1
fi

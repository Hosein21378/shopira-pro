#!/bin/bash

# =============================================
# Shopira Pro - Database Backup Script
# =============================================

BACKUP_DIR="./backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/shopira_backup_$DATE.sql"

mkdir -p "$BACKUP_DIR"

echo "🔄 Starting database backup..."

docker exec shopira-db pg_dump -U shopira shopira > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Backup created successfully: $BACKUP_FILE"
    gzip "$BACKUP_FILE"
    echo "📦 Backup compressed: ${BACKUP_FILE}.gz"
    find "$BACKUP_DIR" -name "shopira_backup_*.sql.gz" -mtime +30 -delete
    echo "🧹 Old backups cleaned up"
else
    echo "❌ Backup failed!"
    exit 1
fi

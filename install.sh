#!/bin/bash

# =============================================
# Shopira Pro - One-Line Installer
# =============================================

set -e

echo "🚀 Shopira Pro Installer"
echo "=========================="
echo ""

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}Please run as root (use sudo)${NC}"
    exit 1
fi

echo -e "${YELLOW}Updating system packages...${NC}"
apt update -y && apt upgrade -y

echo -e "${YELLOW}Installing Docker...${NC}"
curl -fsSL https://get.docker.com | sh

echo -e "${YELLOW}Installing Docker Compose...${NC}"
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

echo -e "${YELLOW}Creating project directory...${NC}"
mkdir -p /opt/shopira-pro
cd /opt/shopira-pro

echo -e "${YELLOW}Downloading Shopira Pro...${NC}"
curl -sSL https://github.com/Hosein21378/shopira-pro/archive/refs/heads/main.tar.gz | tar xz --strip-components=1

echo ""
echo -e "${GREEN}✅ Files downloaded successfully!${NC}"
echo ""

read -p "Enter your Telegram Bot Token: " BOT_TOKEN
while [ -z "$BOT_TOKEN" ]; do
    echo -e "${RED}Bot Token cannot be empty!${NC}"
    read -p "Enter your Telegram Bot Token: " BOT_TOKEN
done

read -p "Enter your Telegram Admin ID (numeric): " ADMIN_ID
while [ -z "$ADMIN_ID" ]; do
    echo -e "${RED}Admin ID cannot be empty!${NC}"
    read -p "Enter your Telegram Admin ID: " ADMIN_ID
done

echo ""
echo -e "${YELLOW}Creating .env file...${NC}"

cat > .env << EOF
BOT_TOKEN=$BOT_TOKEN
ADMIN_ID=$ADMIN_ID

DATABASE_URL=postgresql+asyncpg://shopira:shopira123@db/shopira
REDIS_URL=redis://redis:6379/0

PASARGAD_MERCHANT_CODE=
PASARGAD_TERMINAL_ID=
PASARGAD_CERTIFICATE_PATH=./cert/pasargad_cert.xml
PASARGAD_CALLBACK_URL=https://yourdomain.com/payment/callback

OPENAI_API_KEY=
AI_ENABLED=true

DEBUG=false
LOG_LEVEL=INFO
EOF

echo -e "${GREEN}✅ .env file created!${NC}"

echo ""
echo -e "${YELLOW}Starting Docker containers...${NC}"
docker compose up -d --build

echo ""
echo -e "${GREEN}🎉 Shopira Pro installed successfully!${NC}"
echo ""
echo "📌 Useful commands:"
echo "   View logs:        docker compose logs -f bot"
echo "   Restart bot:      docker compose restart bot"
echo "   Stop everything:  docker compose down"
echo "   Backup database:  ./scripts/backup.sh"
echo ""
echo -e "${YELLOW}Don't forget to add your Pasargad certificate in ./cert/${NC}"

#!/usr/bin/env bash
set -e

PROJECT_NAME="mirocopy-converter"
APP_DIR="$HOME/MiroCopy-Converter"

echo "🚀 Deploy ConverterBot ($PROJECT_NAME)"

cd "$APP_DIR"

echo "📥 Pull latest code"
git pull

echo "🛑 Stop old Converter containers"
docker compose -p "$PROJECT_NAME" down --remove-orphans

echo "🔨 Build & start Converter containers"
docker compose -p "$PROJECT_NAME" up -d --build

echo "🧹 Cleaning up unused Docker images..."
docker image prune -f

echo "✅ Converter deploy finished"

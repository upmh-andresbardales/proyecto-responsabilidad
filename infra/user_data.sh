#!/bin/bash
set -euo pipefail

# ============================================
# User Data - Setup completo para EC2
# Instala Docker, Docker Compose, clona repo y despliega
# ============================================

exec > /var/log/user-data.log 2>&1
echo "=== Inicio de setup: $(date) ==="

# --- Actualizar sistema ---
apt-get update -y
apt-get upgrade -y

# --- Instalar Docker ---
apt-get install -y ca-certificates curl gnupg lsb-release git
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update -y
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# --- Agregar usuario ubuntu al grupo docker ---
usermod -aG docker ubuntu

# --- Clonar repositorio ---
cd /home/ubuntu
git clone ${github_repo} app
chown -R ubuntu:ubuntu app

# --- Crear .env para produccion ---
cd app
cp .env.example .env

# --- Levantar servicios ---
docker compose up --build -d

echo "=== Setup completado: $(date) ==="

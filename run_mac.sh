#!/bin/bash
# ─────────────────────────────────────────────────────────────
#  CUMT 校园网自动登录 — macOS 启动脚本
#  使用方法：双击此脚本，或在终端运行  bash run_mac.sh
# ─────────────────────────────────────────────────────────────

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "======================================"
echo "  CUMT 校园网自动登录 (macOS 版)"
echo "======================================"

# 检测 Python3
if ! command -v python3 &>/dev/null; then
    echo "[错误] 未检测到 python3，请先安装 Python 3.10+"
    echo "下载地址: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "[Python] 版本: $PYTHON_VERSION"

# 安装依赖（若已安装则跳过）
echo "[依赖] 正在检查/安装依赖..."
python3 -m pip install -q -r requirements_mac.txt

echo "[启动] 正在启动程序..."
python3 mac_login_app.py "$@"

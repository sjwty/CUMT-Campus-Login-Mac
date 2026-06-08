# CUMT 校园网自动登录 — macOS 版

> 本项目基于 [MuQY1818/CUMT_Net_Auto_Login](https://github.com/MuQY1818/CUMT_Net_Auto_Login) 移植到 macOS 平台。

---

## ✨ 功能特性

- 🖥️ **菜单栏常驻**：不占 Dock 栏，只在右上角菜单栏显示状态图标
- 🔄 **后台定时检测**：每隔 N 分钟自动检测网络登录状态（默认 5 分钟，可设置）
- ⚡ **断线自动重连**：检测到未登录时自动触发登录，并通过系统通知告知结果
- 📡 **多运营商支持**：校园网 / 中国电信 / 中国移动 / 中国联通
- 🚀 **开机自启**：使用 macOS `launchd` 实现，勾选后开机静默运行
- ⚙️ **可视化设置**：点击菜单栏图标 → 设置，可随时修改账号信息和检测间隔

**菜单栏图标颜色含义：**

| 颜色 | 状态 |
|------|------|
| 🟢 绿色 | 已登录校园网 |
| 🔴 红色 | 未登录 |
| 🟡 黄色 | 正在检测 / 登录中 |

---

## 🖥️ 环境要求

- macOS 11 Big Sur 及以上
- Python 3.9+（系统自带即可）

---

## 🚀 快速开始

### 方式一：直接运行源码（推荐开发者）

```bash
# 1. 安装依赖
pip3 install PySide6 requests

# 2. 运行
python3 mac_login_app.py
```

或使用一键启动脚本：

```bash
bash run_mac.sh
```

### 方式二：打包成 .app（推荐普通用户）

```bash
# 安装打包工具
pip3 install pyinstaller

# 打包
python3 -m PyInstaller cumt_mac.spec --noconfirm

# 清除系统隔离标记（首次运行必须）
xattr -cr dist/CUMT校园网登录.app

# 双击 dist/CUMT校园网登录.app 即可使用
```

---

## 📂 文件说明

| 文件 | 说明 |
|------|------|
| `mac_login_app.py` | 主程序源代码 |
| `requirements_mac.txt` | Python 依赖声明 |
| `run_mac.sh` | 一键启动脚本 |
| `cumt_mac.spec` | PyInstaller 打包配置 |
| `使用说明_mac.txt` | 中文详细说明 |

---

## 📁 配置文件位置

| 类型 | 路径 |
|------|------|
| 账号设置 | `~/Library/Application Support/CUMTAutoLogin/settings.json` |
| 开机自启 | `~/Library/LaunchAgents/com.cumt.autologin.plist` |

---

## 🔧 与原版的主要差异（Windows → macOS）

| 项目 | Windows 原版 | macOS 版 |
|------|-------------|---------|
| GUI 框架 | PyQt5 | PySide6 |
| 开机自启 | Windows 注册表 | launchd plist |
| 配置存储 | QSettings（注册表） | JSON 文件 |
| 应用形态 | 普通窗口程序 | 菜单栏 Agent |
| 后台检测 | 无 | 定时自动检测并重连 |
| Dock 显示 | 有 | 无（LSUIElement=True） |

---

## ⚠️ 注意事项

1. 需要连接矿大校园网（`10.2.5.251` 可达）才能使用登录功能
2. 密码以明文 JSON 形式存储在本地配置文件中，请注意安全
3. 本工具仅供个人便捷上网使用，请遵守学校网络使用规定

---

## 📜 License

基于原项目 [MIT License](https://github.com/MuQY1818/CUMT_Net_Auto_Login/blob/main/LICENSE)

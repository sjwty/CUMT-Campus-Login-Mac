<h1 align="center"> CUMT 校园网自动登录 — macOS 版</h1>

<p align="center">
  <img src="https://img.shields.io/badge/macOS-11%2B-blue?logo=apple" />
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PySide6-GUI-41CD52?logo=qt" />
  <img src="https://img.shields.io/github/license/sjwty/jwt" />
</p>

<p align="center">
  基于 <a href="https://github.com/MuQY1818/CUMT_Net_Auto_Login">MuQY1818/CUMT_Net_Auto_Login</a> 移植到 macOS，支持后台常驻、定时检测、断线自动重连。
</p>

---

##  下载安装（推荐）

> 无需安装 Python，双击即用。

**[ 点击前往 Releases 页面下载 .app](../../releases/latest)**

1. 下载 `CUMT校园网登录.zip`，解压得到 `CUMT校园网登录.app`
2. 将 `.app` 拖入「应用程序」文件夹（可选）
3. **右键 → 打开**（首次需右键打开以绕过 Gatekeeper）
4. 点击菜单栏图标 → ⚙️ 设置 → 填入学号密码 → 保存

---

##  功能特性

| 功能 | 说明 |
|------|------|
|  **菜单栏常驻** | 不占 Dock，只在右上角菜单栏显示状态图标 |
|  **定时自动检测** | 每隔 N 分钟检测登录状态（默认 5 分钟，可调） |
|  **断线自动重连** | 检测到掉线立即重新登录，系统通知告知结果 |
|  **多运营商** | 校园网 / 中国电信 / 中国移动 / 中国联通 |
|  **开机自启** | 勾选后开机静默运行，无需手动打开 |
|  **可视化设置** | 随时修改账号、密码、检测间隔 |

**菜单栏图标颜色：**

| 🟢 绿色 = 已登录 | 🔴 红色 = 未登录 | 🟡 黄色 = 检测/登录中 |

---

##  从源码运行（开发者）

```bash
# 1. 克隆项目
git clone https://github.com/sjwty/jwt.git
cd jwt

# 2. 安装依赖
pip3 install PySide6 requests

# 3. 运行
python3 mac_login_app.py
```

或使用一键脚本（自动安装依赖）：

```bash
bash run_mac.sh
```

### 自行打包 .app

```bash
pip3 install pyinstaller
python3 -m PyInstaller cumt_mac.spec --noconfirm

# 清除隔离标记
xattr -cr dist/CUMT校园网登录.app
```

---

##  配置文件位置

| 类型 | 路径 |
|------|------|
| 账号设置 | `~/Library/Application Support/CUMTAutoLogin/settings.json` |
| 开机自启 | `~/Library/LaunchAgents/com.cumt.autologin.plist` |

---

##  注意事项

- 需连接矿大校园网（`10.2.5.251` 可达）才能登录
- 密码以明文 JSON 存储在本地，请注意安全
- 仅供个人便捷上网，请遵守学校网络规定

---

##  License

MIT License · 基于 [MuQY1818/CUMT_Net_Auto_Login](https://github.com/MuQY1818/CUMT_Net_Auto_Login)

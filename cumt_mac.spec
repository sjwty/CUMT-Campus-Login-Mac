# -*- mode: python ; coding: utf-8 -*-
# CUMT 校园网自动登录 — macOS .app 打包配置

import os

block_cipher = None

# 图标文件路径（使用 _internal 里的 PNG，若有 ICNS 更好）
icon_src = os.path.join('_internal', 'assets', 'icons', 'app.png')

a = Analysis(
    ['mac_login_app.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        # 将 assets 文件夹一并打包进去
        (os.path.join('_internal', 'assets'), 'assets'),
    ],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'requests',
        'urllib3',
        'charset_normalizer',
        'certifi',
        'idna',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'PySide6.QtWebEngineWidgets',
        'PySide6.QtWebEngine',
        'PySide6.QtMultimedia',
        'PySide6.Qt3DCore',
        'PySide6.QtCharts',
        'PySide6.QtDataVisualization',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CUMT校园网登录',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,         # 不显示终端窗口
    disable_windowed_traceback=False,
    argv_emulation=True,   # macOS 需要
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_src if os.path.exists(icon_src) else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CUMT校园网登录',
)

app = BUNDLE(
    coll,
    name='CUMT校园网登录.app',
    icon=icon_src if os.path.exists(icon_src) else None,
    bundle_identifier='com.cumt.autologin',
    info_plist={
        'CFBundleName': 'CUMT校园网登录',
        'CFBundleDisplayName': 'CUMT校园网登录',
        'CFBundleVersion': '1.0.2',
        'CFBundleShortVersionString': '1.0.2',
        'NSHighResolutionCapable': True,
        'NSRequiresAquaSystemAppearance': False,   # 支持深色模式
        'LSUIElement': True,                       # 隐藏 Dock 图标（菜单栏 App）
        'CFBundleDocumentTypes': [],
    },
)

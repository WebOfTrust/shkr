# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['shkr/main.py'],
    pathex=[],
    binaries=[
        ('libsodium.23.arm.dylib', '.'),
        ('libsodium.23.i386.dylib', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='Shkr',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=os.environ['SHKR_SIGNER'],
    entitlements_file='entitlements.plist',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='shkr',
)
app = BUNDLE(
    coll,
    name='shkr.app',
    icon='salt.icns',
    bundle_identifier=os.environ['SHKR_IDENT'],
)

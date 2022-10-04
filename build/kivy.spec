# -*- mode: python ; coding: utf-8 -*-

import sys
import os
from pathlib import Path

from kivy_deps import sdl2, glew

from kivymd import hooks_path as kivymd_hooks_path

path = Path(os.path.abspath('..'))

a = Analysis(
    [path /'main.py'],
    pathex=[path.absolute()],
   	datas=[
		   (path / 'app.py', '.'), 
		   (path / 'main.py', '.'),
		   (path / 'app_config.ini', '.'),
		   (path / 'context.py', '.'),
		   (path / 'widgets/*', 'widgets'),
		   (path / 'structures/*', 'structures'),
		   (path / 'parse_utils/*', 'parse_utils'),
		   (path / 'icon.png', '.')
	   ],
    hookspath=[kivymd_hooks_path],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    debug=False,
    strip=False,
    upx=True,
    name="EducationPlatform",
	icon=str(path / 'icon.ico'),
    console=False,                                                                            
)

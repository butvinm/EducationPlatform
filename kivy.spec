# -*- mode: python ; coding: utf-8 -*-

import sys
import os

from kivy_deps import sdl2, glew

from kivymd import hooks_path as kivymd_hooks_path

path = os.path.abspath(".")

a = Analysis(
    ['main.py'],
    pathex=[path],
   	datas=[
		   ('app.py', '.'), 
		   ('main.py', '.'),
		   ('app_config.ini', '.'),
		   ('context.py', '.'),
		   ('widgets/*', 'widgets'),
		   ('structures/*', 'structures'),
		   ('parse_utils/*', 'parse_utils'),
		   ('icon.png', '.'),
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
	icon='icon.ico',
    console=False,                                                                            
)

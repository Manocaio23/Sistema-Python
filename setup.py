import sys
from cx_Freeze import setup, Executable

include_files = []

base = None

if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(script='Sistema.py', base = base, icon='')


setup(name = "Cadastro",
        version = "0.1",
        description = "this is a script",
        options = {'build_exe':{'include_files':include_files}},
        executables = [exe])

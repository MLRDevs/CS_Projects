# Alex Miller
# Movie Database Executable 

from cx_Freeze import setup, Executable

base = None

executables = [Executable('Movies.py', base=base)]

packages = [
    'idna',
    'openpyxl',
    'random',
    'sys',
    'os',
    'openpyxl.utils'
]

options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = 'MovieDataBase',
    options = options,
    version = '23.8.0.0',
    description = 'MovieDataBase',
    executables = executables 
)
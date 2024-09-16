import shutil
import os

# Указываем путь к исходному файлу и путь к новому файлу
source = 'artists.xlsx'
destination = 'last.xlsx'

# Копируем файл
shutil.copy(source, destination)
import hashlib
import sys
import os
import time
from colorama import Fore, init

# Инициализация Colorama
init(autoreset=True)

# Очистка консоли и установка заголовка (для Windows)
def setup_console():
    if os.name != "nt":
        os.system("clear")
    else:
        os.system("Разработчик » github.com/geniuszlyy")
        os.system("cls")

# Отображение баннера с инструкциями или информацией
def display_banner(mode):
    banner_text = rf"""
{Fore.LIGHTRED_EX}   ____            ____                             _      _         _   _                    
  / ___| ___ _ __ |  _ \  ___  ___ _ __ _   _ _ __ | |_   / \  _   _| |_| |__  _ __ ___   ___ 
 | |  _ / _ \ '_ \| | | |/ _ \/ __| '__| | | | '_ \| __| / _ \| | | | __| '_ \| '_ ` _ \ / _ \
 | |_| |  __/ | | | |_| |  __/ (__| |  | |_| | |_) | |_ / ___ \ |_| | |_| | | | | | | | |  __/
  \____|\___|_| |_|____/ \___|\___|_|   \__, | .__/ \__/_/   \_\__,_|\__|_| |_|_| |_| |_|\___|
                                        |___/|_|                                                                                                                        
    """
    
    help_text = rf"""
        {Fore.LIGHTYELLOW_EX}╭────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╮
        | {Fore.LIGHTGREEN_EX}Use » python GenDecryptAuthme.py [hash] [wordlist]  {Fore.LIGHTYELLOW_EX}| 
        ╰────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╯
    """
    
    if mode == "help":
        print(banner_text + help_text)
    else:
        print(banner_text)

# Начальная установка консоли
setup_console()

# Проверка аргументов командной строки
if len(sys.argv) != 3:
    display_banner(mode="help")
    sys.exit(-1)

# Извлечение хэша и файла со словарем из аргументов командной строки
target_hash = sys.argv[1]
wordlist_file = sys.argv[2]

# Обработка хэша для извлечения соли и основного хэша
if target_hash.startswith("$SHA$"):
    try:
        hash_parts = target_hash.split("$")
        salt = hash_parts[2]
        target_hash = hash_parts[3]
    except IndexError:
        print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Неверный формат хэша.")
        sys.exit(-1)
else:
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Неверный формат хэша. Ожидаемый формат: {Fore.LIGHTGREEN_EX}$SHA$<salt>$<hash>")
    sys.exit(-1)

# Отображение баннера
display_banner(mode="")
print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Загрузка паролей из {Fore.LIGHTCYAN_EX}» {Fore.LIGHTGREEN_EX}{wordlist_file}')

# Загрузка словаря паролей
try:
    with open(wordlist_file, encoding='utf-8', mode='r', errors='ignore') as file:
        passwords = [line.strip() for line in file.readlines()]
    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Загружено {Fore.LIGHTGREEN_EX}{len(passwords)} {Fore.LIGHTBLUE_EX}слов из {Fore.LIGHTGREEN_EX}{wordlist_file}')
except FileNotFoundError:
    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Ошибка: файл словаря не найден.')
    sys.exit(-1)
except Exception as e:
    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Ошибка загрузки словаря: {str(e)}.')
    sys.exit(-1)

# Начало отсчета времени
start_time = time.time()

# Перебор паролей из словаря для поиска совпадения
attempt_count = 0
for password in passwords:
    attempt_count += 1
    # Генерация хэша для пароля с использованием соли
    hashed_password = hashlib.sha256(hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8') + salt.encode('utf-8')).hexdigest()
    if hashed_password == target_hash:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Пароль найден {Fore.LIGHTCYAN_EX}» {Fore.LIGHTGREEN_EX}{password}')
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Время поиска: {Fore.LIGHTGREEN_EX}{elapsed_time:.2f} {Fore.LIGHTBLUE_EX}секунд')
        sys.exit(0)
end_time = time.time()
elapsed_time = end_time - start_time
print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Пароль не найден')
print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDecryptAuthme {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}Время поиска: {Fore.LIGHTGREEN_EX}{elapsed_time:.2f} {Fore.LIGHTBLUE_EX}секунд')

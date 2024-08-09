# GenDecryptAuthme
 A Python tool for decrypting passwords hashed with the AuthMe SHA256 algorithm. Ideal for penetration testing and security audits on Minecraft servers using the AuthMe authentication plugin.

# EN
## Overview

The GenDecryptAuthme is a Python script designed to decrypt passwords hashed using the AuthMe SHA256 algorithm. This tool is particularly useful for those looking to perform penetration testing or security audits on Minecraft servers utilizing the AuthMe authentication plugin.

## Features

- Supports AuthMe SHA256 hashing algorithm.
- Reads a wordlist to perform brute-force attacks.
- Displays the time taken to find the password.
- Provides detailed error messages and usage instructions.

## Requirements

- Python 3.x
- `colorama` module

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/geniuszlyy/GenDecryptAuthme.git
    cd GenDecryptAuthme
    ```

2. **Install the required module:**

    ```sh
    pip install colorama
    ```

## Usage

1. **Prepare your wordlist:**

    Create a text file (e.g., `wordlist.txt`) with each potential password on a new line.

2. **Run the script:**

    ```sh
    python main.py '$SHA$salt$hash' wordlist.txt
    ```

    - Replace `salt` and `hash` with the appropriate values.
    - Ensure the hash is in the format: `$SHA$salt$hash`.

3. **Example:**

    ```sh
    python main.py '$SHA$69ac426df8b3af1b19a73bc24ad4b94c878de0aa9f1fb6c8a68826f1d0c04072' wordlist.txt
    ```
    ![image](https://github.com/user-attachments/assets/bde12102-86a9-4df5-9eb5-b2e2f99b5a76)

    ![image](https://github.com/user-attachments/assets/fd33d207-4dab-4a4f-962d-57b24ae743d2)
   
## Output

- If the password is found, the script will display the password along with the time taken to find it.
- If the password is not found, the script will inform you and display the time taken for the search.


# RU 
## Обзор

GenDecryptAuthme — это скрипт на Python, предназначенный для декриптирования паролей, хэшированных с использованием алгоритма AuthMe SHA256. Этот инструмент особенно полезен для тех, кто хочет провести тестирование на проникновение или аудит безопасности на серверах Minecraft, использующих плагин аутентификации AuthMe.

## Особенности

- Поддержка хэширования с использованием алгоритма AuthMe SHA256.
- Чтение списка слов для выполнения атак методом грубой силы.
- Отображение времени, затраченного на нахождение пароля.
- Предоставление подробных сообщений об ошибках и инструкций по использованию.

## Требования

- Python 3.x
- Модуль `colorama`

## Установка

1. **Клонируйте репозиторий:**

    ```sh
    git clone https://github.com/geniuszlyy/GenDecryptAuthme.git
    cd GenDecryptAuthme
    ```

2. **Установите необходимый модуль:**

    ```sh
    pip install colorama
    ```

## Использование

1. **Подготовьте ваш список слов:**

    Создайте текстовый файл (например, `wordlist.txt`), в котором каждый потенциальный пароль будет на новой строке.

2. **Запустите скрипт:**

    ```sh
    python main.py '$SHA$salt$hash' wordlist.txt
    ```

    - Замените `salt` и `hash` на соответствующие значения.
    - Убедитесь, что хэш находится в формате: `$SHA$salt$hash`.

3. **Пример:**

    ```sh
    python main.py '$SHA$69ac426df8b3af1b19a73bc24ad4b94c878de0aa9f1fb6c8a68826f1d0c04072' wordlist.txt
    ```
    ![image](https://github.com/user-attachments/assets/bde12102-86a9-4df5-9eb5-b2e2f99b5a76)

    ![image](https://github.com/user-attachments/assets/fd33d207-4dab-4a4f-962d-57b24ae743d2)



## Вывод

- Если пароль найден, скрипт отобразит пароль вместе с временем, затраченным на его нахождение.
- Если пароль не найден, скрипт сообщит об этом и покажет время, затраченное на поиск.

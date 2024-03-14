product_id, title, characteristics, price, old_price, discount

## Как начать

### 1. Настройка Git

Убедитесь, что Git установлен на вашем компьютере. Если нет, вы можете [скачать его с официального сайта Git](https://git-scm.com/). Откройте терминал или командную строку.

### 2. Склонируйте репозиторий:

```bash
git clone https://github.com/suer-tech/ym_parser.git
```
### 3. Перейдите в каталог проекта.
### 4. Установите инструмент virtualenv (если его нет):
```bash
pip install virtualenv
```
### 5. Создайте виртуальное окружение.
Перейдите в каталог вашего проекта в терминале.
Выполните команду для создания виртуального окружения:
```bash
virtualenv venv
```
### 6. Активируйте виртуальное окружение:
На Windows:
```bash
venv\Scripts\activate
```

На Linux или macOS:
```bash
source venv/bin/activate
```
### 7. Установите зависимости:

После активации виртуального окружения, выполните установку зависимостей
```bash
pip install -r requirements.txt
```
### 8. Запуск:

Выполните команду для запуска:
```bash
python main.py
```

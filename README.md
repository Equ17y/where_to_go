# Куда пойти — Москва глазами Артёма

Интерактивная карта с описаниями интересных мест Москвы.

![Скриншот](screenshot.png)

## Возможности

- Просмотр локаций на интерактивной карте
- Детальные описания с HTML-форматированием
- Удобная админ-панель для управления контентом:
  - drag-and-drop сортировка изображений
  - WYSIWYG-редактор для описаний
  - превью загруженных фотографий

## Требования

- Python 3.13.3

## Переменные окружения

Перед запуском проекта необходимо настроить следующие переменные окружения в файле `.env`:

### Обязательные переменные

**`SECRET_KEY`** — секретный ключ для конкретной установки Django. Используется для криптографической подписи и должен быть уникальным и непредсказуемым значением.

```bash
SECRET_KEY=django-insecure-ваш-уникальный-секретный-ключ-из-50-символов
```

**`DEBUG`** — булево значение, включающее/отключающее режим отладки. Если при **`DEBUG=True`** возникает исключение, Django отображает детальный traceback с метаданными среды.

```bash
DEBUG=True
```

**`ALLOWED_HOSTS`** — список доменных имён, которые может обслуживать этот Django-сайт. Защита от атак через HTTP Host header.

```bash
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Установка и запуск

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Equ17y/where_to_go.git
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    venv\Scripts\Activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск локально

1. Установите зависимости (если ещё не установлены):

    ```bash
    pip install -r requirements.txt
    ```

2. Создайте файл `.env` на основе примера в `.env.example`:

    ```bash
    SECRET_KEY=ваш_секретный_ключ
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    ```

3. Выполните миграции и запустите сервер:

    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```

4. Откройте в браузере: http://127.0.0.1:8000

## Загрузка данных

Для загрузки локации из JSON-файла выполните команду:

```bash
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/moscow_legends.json
```

## Технологии

- Python 3.10+
- Django 5.0
- PostgreSQL / SQLite (для разработки)
- Leaflet.js + Vue.js (фронтенд)
- Bootstrap 4
- `django-admin-sortable2`
- `django-tinymce`
- `environs` для безопасных настроек
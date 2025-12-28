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

## Обязательные переменные

**`SECRET_KEY`** — секретный ключ для конкретной установки Django. Используется для криптографической подписи и должен быть уникальным и непредсказуемым значением.

```bash
SECRET_KEY=django-insecure-ваш-уникальный-секретный-ключ-из-50-символов
```

**`DEBUG`** — булево значение, включающее/отключающее режим отладки. Если при **`DEBUG=True`** возникает исключение, Django отображает детальный traceback с метаданными среды. Всегда устанавливайте DEBUG=False на продакшн-сервере!

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

- Выполните миграции базы данных:

    ```bash
    python manage.py migrate
    ```

- Создайте суперпользователя для доступа к админ-панели:

    ```bash
    python manage.py createsuperuser
    ```

- Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

4. Откройте в браузере:

- Приложение: http://127.0.0.1:8000
- Админ-панель: http://127.0.0.1:8000/admin

## Загрузка данных

Особенности и и пример запуска скрипта `load_place`:

- Формат JSON-файла:

```json
{
    "title": "Название места",
    "imgs": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
    "description_short": "Краткое описание",
    "description_long": "<p>Полное описание с HTML-разметкой</p>",
    "coordinates": {
        "lng": "37.6173",
        "lat": "55.7558"
    }
}
```

- Пример запуска:

```bash
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/moscow_legends.json
Created place: Экскурсионная компания «Легенды Москвы»
  Added image: 4f793576c79c1cbe68b73800ae06f06f.jpg
  Added image: 7a7631bab8af3e340993a6fb1ded3e73.jpg
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
# load_all_places.py
import os
import sys

import django

from places.management.commands.load_place import Command

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'where_to_go.settings')
django.setup()


def main():
    if len(sys.argv) != 2:
        print('Использование: python load_all_places.py <файл_с_URL.txt>')
        sys.exit(1)

    urls_file = sys.argv[1]
    with open(urls_file, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]

    command = Command()
    total = len(urls)
    for i, url in enumerate(urls, 1):
        print(f'\n[{i}/{total}] Загрузка: {url}')
        try:
            command.handle(url=url)
        except Exception as e:
            print(f'  ❌ Ошибка: {e}')

    print(f'\n Успешно загружено {total} локаций!')


if __name__ == '__main__':
    main()

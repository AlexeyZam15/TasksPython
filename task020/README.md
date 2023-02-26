## Задачи
1. Создать из task019 python package и загрузить на pypi.org или test.pypi.org
2. Создать виртуальное окружение
3. Установить пакет в виртуальном окружении
4. Проверить работоспособность

### Команды для создания и загрузки пакета Python
1. Проверка корректности установки локального пакета - pip install .
2. Подготовка пакета Python к загрузке - python -m build
3. Загрузка на тестовую версию pypi.org - python -m twine upload --repository testpypi dist/*
4. Загрузка на pypi.org - python -m twine upload --repository pypi dist/*
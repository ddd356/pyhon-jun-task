# python-jun-task

Привет!

Это тестовое задание Python Джуна.

Сервер работает на [Flask](https://flask.palletsprojects.com/en/2.2.x/).

База данных [TinyDB](https://tinydb.readthedocs.io/en/latest/).

Сначала подготовим виртуальное окружение, в котором будет запускаться наша программа.
```
python -m venv jun-task
cd jun-task
source bin/activate
```

Кроме модулей, которые есть в стандартной либе может понадобиться установить tinydb и flask
```
pip install tinydb
pip install flask
```
Перемещаем файлы проекта в каталог виртуального окружения

Файлы в этом проекте:
- app.py        - главный файл программы
- test-app.py   - юнит-тесты с использованием unittest
- db.json       - база с тестовыми данными
- README.md     - этот файл
- request.sh    - скрипт с тестовыми запросами


Итак, выполним тестирование нашего сервера:

Запускаем Flask. Хост и порт можно указать те, которые нам нужны
```
flask run --host 127.0.0.1 --port 5000
```
Делаем запрос curl-ом
```
curl --request POST --header 'Content-Type: application/json' --data '{"fname1": "email@site.com", "fname2":"some text"}' 'http://127.0.0.1:5000'
```
Видим, что в базе нашелся подходящий шаблон. Имя шаблона: *form1*. Типы полей: *email* и *text*.
```
[{"form_name": "form1", "fname1": "email", "fname2": "text"}] 
```
Теперь попробуем сделать запрос, для которого в нашей базе не будет подходящего шаблона:
```
curl --request POST --header 'Content-Type: application/json' --data '{"impossible_field_name1": "bad@mail.com", "impossible_field_name2":"something mystical"}' 'http://127.0.0.1:5000'
```
в ответ получаем список полей с их типами
```
{"impossible_field_name1":"email","impossible_field_name2":"text"}
```
Тестовые запросы собраны в скрипте request.sh. Перед его запуском понадобится разрешить исполнение:
```
chmod +x request.sh
```
```
./request.sh
```

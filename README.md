# Пульт охраны банка

Программа позволяет просматривать на сайте список активных карт доступа, людей в хранилище на текущие время, а так же отображает список всех посещений хранилища по пропуску.  

### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```console
pip install -r requirements.txt
```

### Первоначальная настройка
Python3 должен быть уже установлен.  
Скопируйте файл `.env.Example` из папки `project` и переименуйте его в `.env`.  

Заполните переменные окружения в файле `.env`:  
`ALLOWED_HOSTS` - Разрешенные хосты. Указываются через запятую, например: `127.0.0.1,localhost`.  
`DB_URL` - Адрес сервера базы данных в формате `postgres://USER:PASSWORD@HOST:PORT/NAME`.  
`SECRET_KEY` - Секретный ключ.  
`DEBUG` - Если нужно включить режим отладки web-сервера, установите значение в `True`.  


### Как запускать
```console
python manage.py runserver 0.0.0.0:8000
```

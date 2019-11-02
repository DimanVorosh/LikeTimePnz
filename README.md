# Like Time Pnz

Приложение для автоматического сбора урожая

### Конфигурация nginx

```nginx
map $http_upgrade $connection_upgrade {
default upgrade;
‘’ close;
}

upstream frontend {
server 127.0.0.1:8080;
}

upstream backend {
server 127.0.0.1:8000;
}

server {
listen 80;
server_name moon.local;
client_max_body_size 100M;

location /api {
proxy_pass http://backend/;
proxy_set_header Host 127.0.0.1;
}

location / {
proxy_pass http://frontend/;
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection “upgrade”;
proxy_set_header Host 127.0.0.1;
}
}
```

Для сборки проекта необходимы такие пакеты как redis, postgresql, npm, nodejs

### backend

В корне в файле config.py в объекте POSTGRESQL поле username на свое имя пользователя в postgres

```bash
psql postgres
postgres=# create database liketimepnz;
postgres=# \q

cd backend
python3 -m venv env
./env/bin/pip3 install - r requirements.txt
alembic upgrade head # запуск миграций
./env/bin/python3 ./init_dt.py # запуск генерации тестовых значений
./dev.sh # запуск (gunicorn)
```

### frontend

```bash
cd frontend
npm install
npm run serve
```

## Описание API

[GET] /api/ - API check

[POST] /login - Вход для инспектора

```json
{
"login": "denis",
"password: 29993643634
}
```
Логин и пароль для инспектора будет в консоли при запуске скрипта для заполнения БД

[GET] /users/current - Получение текущего пользователя

[GET] /logout - Выход

[GET] /activity?date=2019-01-01 - Получение активности рабочих за выбранную дату

## Решения и логика

Было сделано предположение, что существуют два типа пользователя (сборщик и инспектор). 
Был создан прототип Админ-панель, через которую инспекторы контролируют процесс сбора урожая.
То есть сборщик делает запись о том, что закончил сбор урожая, а в свою очередь инспектор записывает, сколько килограммов урожая было собрано. 
Была сделана авторизация для инспекторов. 
Таблица Content-Type была удалена, так как её назначение не ясно, либо в данном кейсе она не требуется.

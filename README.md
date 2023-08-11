# Reviewer
Reviewer - это веб-сайт, позволяющий подобрать фильм для просмотра благодаря развернутым и точным оценкам, либо оставить отзыв самому.

## Установка:

Для того, чтобы проделать следующие шаги на Windows, установите [Git Bash](https://gitforwindows.org/)

1. Склонируйте репозиторий

```shell
git clone https://github.com/F0RRZZ/reviewer.git
```

2. Скачайте и установите Docker

Скачать и найти инструкцию по установке вы можете на официальном сайте [Docker](https://www.docker.com)

3. Запустите сайт в Docker

Для этого откройте терминал и перейдите в папку репозитория

```shell
cd reviewer
```

Войдите в корневую директорию проекта

```shell
cd reviewer
```

#### ! Перед тем, как собрать докер контейнеры, измените файл .env.docker на нужные значения. Либо измените его из командной строки контейнера (как в нее войти будет сказано дальше) !

---

#### Переменные окружения в .env

Описание:
1. ALLOWED_HOSTS - список разрешенных хостов
2. DEBUG - режим отладки
3. EMAIL_ADDRESS - адрес электронной почты, с которой будут приходить письма пользователям
4. EMAIL_PASSWORD - пароль от приложения
5. REDIS_HOST - сервер, на котором запущен Redis
6. REDIS_PORT - порт для взаимодействия с Redis
7. SECRET_KEY - секретный ключ
8. USERS_AUTOACTIVATE - режим автоактивации пользователей (отключение подтверждения аккаунта)
9. DB_NAME - имя базы данных PostgreSQL
10. DB_USER - имя админа PostgreSQL
11. DB_PASSWORD - пароль от базы данных PostgreSQL

Настройка аккаунта Google для отправки сообщений:
1. Создайте новый аккаунт
2. Впишите адрес электронной почты в переменную EMAIL_ADDRESS в .env.docker
3. Перейдите во вкладку "Безопасность" в управлении аккаунтом
4. Включите двухэтапную аутентификацию
5. Перейдите в раздел "Пароли приложений"
6. В поле "Приложение" выберите YouTube, а в "Устройство" - компьютер Windows
7. Нажмите на кнопку "Создать"
8. Полученный ключ впишите в переменную EMAIL_PASSWORD в .env.docker

Далее введите команду

```shell
docker-compose up --build
```

4. Создайте суперпользователя

После того как вы запустили сайт в Docker нужно создать суперпользователя для доступа в панель администратора

Для начала нам нужно узнать ID контейнера, в котором запущен веб-сервер

```shell
docker ps -a
```

В данном списке найдите контейнер с именем reviewer-web и скопируйте CONTAINER ID

Далее введите команду

```shell
docker exec -it <container_id> sh
```

Вместо <container_id> вставьте раннее скопированный ID

После ввода данной команды вам должен быть предоставлен доступ к командной строке контейнера

Вам нужно ввести команду:

```shell
python manage.py createsuperuser
```

И ввести данные суперпользователя

Теперь вы можете зарегистрироваться по данным, введенным раннее и получить доступ к панеле администратора

5. Примените фикстуры (не обязательно)

Если вы хотите загрузить тестовые данные вы можете применить фикстуры

Для этого в терминале контейнера введите команду:

```shell
python manage.py loaddata data.json
```

Готово! Сервер запущен.
Чтобы зайти на сайт перейдите по ссылке: localhost:8000

Чтобы остановить работу контейнеров, в терминале, откуда вы запускали docker-compose нажмите Ctrl+C (Control + C для Mac)

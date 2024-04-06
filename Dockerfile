# Основываемся на официальном образе Python
FROM python:3.12

# Настраиваем рабочую директорию внутри образа
WORKDIR /KINOLIB
COPY * /KINOLIB

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt update && apt-get upgrade -y
RUN apt-get install -y nodejs
RUN pip install django
RUN python -m pip install django-tailwind
RUN pip install django_browser_reload

WORKDIR /KINOLIB/other/static_src
RUN npm i

RUN npm install -D tailwindcss postcss autoprefixer

# Устанавливаем зависимости Python
#RUN pip install -r requirements.txt
#RUN python manage.py tailwind install
#
#RUN python manage.py tailwind start
WORKDIR /KINOLIB


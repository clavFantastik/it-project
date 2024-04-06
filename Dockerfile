# Основываемся на официальном образе Python
FROM python:3.12

# Настраиваем рабочую директорию внутри образа
WORKDIR /KINOLIB
COPY * /KINOLIB

# Устанавливаем nodejs
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt update && apt-get upgrade -y
RUN apt-get install -y nodejs

# Устанавливаем зависимости Python
RUN pip install -r requirements.txt

# Устанавливаем зависимости nodejs
WORKDIR /KINOLIB/other/static_src
RUN npm i


WORKDIR /KINOLIB


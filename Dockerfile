# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install -r requerment.txt

# Команда для запуска приложения
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]

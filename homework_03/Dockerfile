# Для запуска докер контрейнера выполните команду =>>  docker run -p 8000:8000 -it app
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r  requirements.txt
COPY main.py ping_view.py /app/
CMD ["uvicorn", "main:app","--host","0.0.0.0", "--port","8000"]
EXPOSE 8000

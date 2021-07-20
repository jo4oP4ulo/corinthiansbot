FROM python:3.8

ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY *.txt .

RUN pip install --no-cache-dir -r requirements.txt
CMD python3 bot.py

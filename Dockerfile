FROM python:3.8

ENV PYTHONUNBUFFERED True

RUN pip install --no-cache-dir -r requirements.txt
CMD python3 bot.py

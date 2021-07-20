FROM python:3.8

ENV PYTHONUNBUFFERED True
RUN git clone https://github.com/jo4oP4ulo/corinthiansbot.git

RUN pip install --no-cache-dir -r requirements.txt
CMD python3 bot.py

FROM python:3.8

ENV PYTHONUNBUFFERED True

RUN git clone clone https://github.com/jo4oP4ulo/corinthiansbot.git /root/corinthiansbot
WORKDIR /root/corinthiansbot/

# install main requirements.
RUN pip3 install --no-cache-dir -r requirements.txt


CMD python3 bot.py

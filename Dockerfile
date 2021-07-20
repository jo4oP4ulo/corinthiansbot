FROM python:3.8

ENV PYTHONUNBUFFERED True

RUN git clone clone https://github.com/jo4oP4ulo/corinthiansbot.git /root/corinthians
WORKDIR /root/corinthians/

# install main requirements.
COPY requirements.txt /deploy/
RUN pip3 install --no-cache-dir -r /deploy/requirements.txt


RUN pip install --no-cache-dir -r requirements.txt
CMD python3 bot.py

from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from parser import MeuTimao
import re
import youtube_dl
import json
import httpx
import os
import config

async def feed_meu_timao():
    chat_id = -1001063261019
    file_id = 0
    mt = MeuTimao()
    l = mt.last_news()
    id_noticia = int(re.findall('[0-9]+', l.url)[0])

    try:
        with open("noticia.id", 'r') as f:
            id_noticia_ant = int(f.read())
    except FileNotFoundError:
        id_noticia_ant = -1

    print(id_noticia, id_noticia_ant)

    if id_noticia != id_noticia_ant:
        if l.video:
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'outtmpl': '%(id)s.%(ext)s'
            }

            ydl = youtube_dl.YoutubeDL(ydl_opts)

            with ydl:
                result = ydl.extract_info(
                    l.video
                    ,
                    download=False # We just want to extract the info
                )

            if 'entries' in result:
                # Can be a playlist or a list of videos
                video = result['entries'][0]
            else:
                # Just a video
                video = result

            id_v = video['id']

            # try:
            #     data = json.load(open("noticia.json",'r'))
            # except FileNotFoundError:
            #     data = {}
            # file_id = 1

            if True:
                ldir = os.listdir()
                with ydl:
                    result = ydl.extract_info(
                        l.video,
                        download=True # We just want to download the video
                    )

                for filer in ldir:	
                    if id_v in filer:
                        file_id = filer

            r = httpx.get(l.img_url)

            with open("thumb.jpeg",'wb') as f:
                f.write(r.content)


            print(file_id)

            v = await app.send_video(chat_id,
                video=file_id, 
                supports_streaming=True,
                thumb="thumb.jpeg",
                caption=l.title,
            )


            data = {
                    "id":l.noticia_id,
                    "video":v.video.file_id
            }

            json.dump(obj=data,
                    fp=open("noticia.json","w"), 
                    indent=4
            )

            os.remove(file_id)
            os.remove("thumb.jpeg")

        else:
            v = await app.send_photo(chat_id,
                photo=l.img_url,
                caption=f"{l.title}\n\n{l.summary} <a href={l.url}>ler completo</a>",
            )

        with open("noticia.id", 'w') as f:
            f.write(str(id_noticia))

       #print(v)

scheduler = AsyncIOScheduler()
scheduler.add_job(feed_meu_timao, "interval", seconds=5*60)


plugins = dict(
    root="plugins",
)

app = Client(
    "my_bot",
    api_id = config.login.api_id,
    api_hash = config.login.api_hash,
    bot_token='TOKEN API BOT',
    plugins=plugins,
)

scheduler.start()
if __name__ == '__main__':
    app.run()

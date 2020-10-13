import httpx
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto, InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram import Client, filters
import parser
import threading
import youtube_dl
import os
import json

def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

@Client.on_message(filters.command("u_noticia"))
async def u_noticia(client, message):
	mt = parser.MeuTimao()
	l = mt.last_news()


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
		
		try:
			data = json.load(open("noticia.json",'r'))
		except FileNotFoundError:
			data = {}
		file_id = data.get("video")

		if not file_id:
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
		
		v = await message.reply_video(file_id, 
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

		return 

	await message.reply_photo(
		photo=l.img_url,
		caption=f"{l.title}\n\n{l.summary} <a href={l.url}>ler completo</a>",
	)

	data = {
		"id":l.noticia_id,
		"video":None,
	}

	json.dump(obj=data,
		 fp=open("noticia.json","w"), 
		 indent=4
	)

@Client.on_message(filters.command("noticias"))
async def noticias(client, message):
	mt = parser.MeuTimao()
	news = mt.all_news()[:5]
	sep = "\n"
	l = [f"<b>{new.title}</b>\n\n{new.summary} <a href={new.url}>ler completo</a>" for new in news]

	await message.reply(f"<b>Ultimas do CORINTHIANS</b>\n\n {sep.join(l)}",
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➕ noticias", switch_inline_query='')]])
	)

@Client.on_inline_query()
async def query(client, message):
	mt = parser.MeuTimao()
	news = mt.all_news()[:50]
	
	r = [InlineQueryResultArticle(

				title=new.title,
				description=new.summary,
				thumb_url=new.img_url,
				input_message_content=InputTextMessageContent(
				 	disable_web_page_preview=True,
					message_text=f"<b>{new.title}</b>\n\n{new.summary} <a href={new.url}>ler completo</a>"
				 ),
				
				
				reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➕ noticias", switch_inline_query='')]])            
			) for new in news]
	
	await message.answer(r, 
		cache_time=1,
		is_gallery=False,
	)

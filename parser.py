import feedparser
import json
import re


url_main = "https://www.meutimao.com.br/"

class FNoticia:
	def __init__(self, title, summary, url, img_url=None, video_url=None):
		self.title = title
		self.summary = summary
		self.url = url
		self.video = video_url
		self.img_url = "https://"+img_url #url exemplo de entrada : cdn.meutimao.com.br/_upl...
		self.noticia_id = int( re.findall('[0-9]+', url)[0] )

class MeuTimao:
	def __init__(self):
		self.url_rss = url_main+"rss/"

	def parser(self):
		return feedparser.parse(self.url_rss)

	def last_news(self):
		u = self.parser()
		#json.dump(u,fp=open("todo.json",'w'), indent=4) #debug :)
		last = u.entries[0]
		title = last.title
		summary = last.summary
		link = last.link
		midia_url = last.links[1].href[2:]
		content = last.content[0].value

		#print(title)
		#print(summary)
		#print(link)
		#print(url_midia)

		video_url = None
		find = re.search(r'https://www.youtube.com\/([\w\-]+)(\S+)?(amp+)', content)
		if find:
			a, b=find.span()
			video_url = content[a:b]

		return FNoticia(title, summary, link, midia_url, video_url)


	def all_news(self):
		al = self.parser().entries
		news = []
		for info in al:
			title = info.title
			summary = info.summary
			link = info.link
			url_midia = info.links[1].href[2:]
			news.append(FNoticia(title, summary, link, url_midia))

		return news

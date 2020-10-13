![.](https://user-images.githubusercontent.com/27656032/95815250-a8e30000-0cf2-11eb-88be-ed74d864359b.png)


# CorinthiansRobot
### Esse projeto representa minha paixão por programação e futebol, a ideia do mesmo é automatiza o envio de noticias  do clube de futebol Corinthians toda vez que tiver uma notícia nova para um [canal](https://t.me/PaixaoCorinthiana) no Telegram
# Como funciona
### Através do [feed](https://www.meutimao.com.br/rss) é utilizado a biblioteca feedparser e APScheduler, é feito uma automatização onde é buscados os feeds e o bot envia para o canal dentro de um tempo determinado

# Requirements

- APScheduler==3.6.3
- feedparser==5.2.1
- httpx==0.14.2
- TgCrypto==1.2.1
- youtube-dl==2020.7.28
- https://github.com/pyrogram/pyrogram/archive/master.zip

# IMPORTANTE
### para o funcionamento do bot é necessário obter o `api_id` e `api_hash` pode ser encontrado [aqui](https://my.telegram.org/auth)

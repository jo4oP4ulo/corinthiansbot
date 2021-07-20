import os

class message:
    START = """Oi {}, eu sou um bot do <b>Bando de Loucos</b> 🤘🦅
<b>Meus Comandos </b>\n
* /start - <b>Mostra essa mensagem</b>
* /noticias - <b>Envia as noticias mais recentes do Corinthians</b>
* /u_noticia - <b>Envia uma noticia de ultima hora</b>
"""

class login:
    api_id = int(os.environ.get("api_id"))
    api_hash = os.environ.get("api_hash")
    token_bot = os.environ.get("token_bot")

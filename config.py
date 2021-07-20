import os

class message:
    START = """Oi {}, eu sou um bot do bando de loucos 🤘🦅
<b>Meus Comandos </b>\n
* /start - <b>mostra essa mensagem</b>
* /noticias - <b>envia  as ultimas noticias do Corinthians</b>
* /u_noticia - <b>envia uma notica de ultima hora </b>
"""

class login:
    api_id = int(os.environ.get("api_id"))
    api_hash = os.environ.get("api_hash")
    token_bot = os.environ.get("token_bot")

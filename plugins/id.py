from pyrogram import Client, filters

@Client.on_message(filters.command("id"))
async def start(client, message):
    await message.reply("""
<b>Sobre você</b>\n
<b>Nome</b>: <code>{}</code>
<b>ID</b>: <code>{}</code>
    """.format(message.from_user.first_name,message.from_user.id))

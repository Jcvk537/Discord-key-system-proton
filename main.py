import os
print("VARIABILE DISCORD_BOT_TOKEN:", os.getenv("DISCORD_BOT_TOKEN"))
exit()


import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Dizionario chiavi: {user_id: key}
keys = {}

# Comandi

@bot.event
async def on_ready():
    print(f"Bot connesso come {bot.user}")

@bot.command(name="genkey")
async def genkey(ctx, user_id: int):
    key = "666"  # Qui puoi cambiare per generare key dinamiche o da database
    keys[user_id] = key
    await ctx.send(f"Chiave generata per <@{user_id}>: `{key}` 🔑")

@bot.command(name="getkey")
async def getkey(ctx, user_id: int):
    key = keys.get(user_id)
    if key:
        await ctx.send(f"La key per <@{user_id}> è `{key}` 🔍")
    else:
        await ctx.send(f"Nessuna key trovata per <@{user_id}> ❌")

@bot.command(name="checkkey")
async def checkkey(ctx, user_id: int, key: str):
    real_key = keys.get(user_id)
    if real_key == key:
        await ctx.send(f"La key `{key}` per <@{user_id}> è valida ✅")
    else:
        await ctx.send(f"La key `{key}` per <@{user_id}> non è valida ❌")

@bot.command(name="listkeys")
async def listkeys(ctx):
    if not keys:
        await ctx.send("Non ci sono key generate ancora 📭")
        return
    msg = "**Lista key generate:**\n"
    for uid, k in keys.items():
        msg += f"<@{uid}>: `{k}`\n"
    await ctx.send(msg)

@bot.command(name="delkey")
async def delkey(ctx, user_id: int):
    if user_id in keys:
        del keys[user_id]
        await ctx.send(f"Key per <@{user_id}> rimossa 🗑️")
    else:
        await ctx.send(f"Nessuna key trovata per <@{user_id}> ❌")

@bot.command(name="help")
async def help_command(ctx):
    help_msg = """
**Comandi disponibili:**
`!genkey <user_id>` - Genera una key per l'utente
`!getkey <user_id>` - Mostra la key dell'utente
`!checkkey <user_id> <key>` - Controlla se la key è valida per l'utente
`!listkeys` - Mostra tutte le key generate
`!delkey <user_id>` - Rimuove la key dell'utente
`!help` - Mostra questo messaggio
"""
    await ctx.send(help_msg)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Ciao, Render funziona!"

ifconst express = require('express')
const app = express()
const port = process.env.PORT || 4000 

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

import discord
import asyncio
import re
from twitterlib import Twitter
from random import randint

consumer_key = 'consumer key'
consumer_secret = 'consumer secret'

token_access = 'token access'
token_secret = 'token secret'

twitter_client = Twitter(consumer_key, consumer_secret, token_access, token_secret)
client = discord.Client()

#Ligar
@client.event
async def on_ready():
    print('--- Ligado! ---')

#Quando Escrever Mensagens
@client.event
async def on_message(message):

    admins = [400770067559612426, 387674761746186260, 374342024020754434]
    user = message.author.id
    member = message.author
    bot = client.get_channel(786707801984204821)
    cor = 0x690FC3

    def canal_mensagem():
        if message.channel == bot:
            return True
        else:
            return False
    
    def has_permission(): # QUE VERGONHA DE TER FEITO ESSE TIPO DE COISA HAHAHAHAHAHA
        sim = "nao"
        for i in admins:
            if user == i:
                sim = "sim"
                break
        if sim == "sim":
            return True
        else:
            return False

    def bloqueado():
        return False
    
    # !twitter || Desativado
    if message.content.lower().startswith('!twitter'):
        if not bloqueado():
            args = message.content.rsplit(" ", -1)
            if len(args) == 1:
                msg = '--> {} Especifique um argumento (pesquisar)'.format(member.mention)
                await message.channel.send(msg)
            if len(args) == 2:
                msg = '--> {} Especifique as palavras-chave!'.format(member.mention)
                await message.channel.send(msg)
            if len(args) > 2:
                if args[1] == 'pesquisar': #0 = !twitter | 1 = metodo | 2 = keywords
                    termo = ""
                    contador = 0
                    for arg in message.content:
                        contador += 1
                        if contador > 18:
                            termo = termo + arg
                    resposta = twitter_client.search(termo)
                    try:
                        nome = "Autor: " + resposta[0]["user"]["screen_name"]
                        tweet = "\nPost:\n-------------------------\n" + resposta[0]["text"] + "\n-------------------------"
                        favs = str(resposta[0]["favorite_count"])
                        fav = "\n:heart:: " + favs
                        resposta = nome + fav + tweet
                        padrao = re.search(r'https://t.co/\w\w\w\w\w\w\w\w\w\w', resposta) # hahahahahahah nunca mais faço isso
                        embed = discord.Embed(
                                            title="**Pesquisa Twitter**",
                                            color=cor,
                                            description=resposta)
                                            
                        await message.channel.send(embed=embed)
                        if padrao != None:
                            await message.channel.send(padrao.group())
                    except IndexError:
                        await message.channel.send("--> {} Pesquisa: `{}` não encontrada =(".format(message.author.mention, termo))
                        
        else:
            msg = '--> {} Comando Desativado!'.format(member.mention)
            await message.channel.send(msg)
    
    # !ajuda
    if message.content.lower().startswith('!ajuda'):
        if canal_mensagem() or has_permission():
            resposta = discord.Embed(title='**Ajuda**',
                                    color=cor,
                                    description='')
            resposta.add_field('!ip', 'IP do servidor!', True)
            resposta.add_field('!loja', 'Loja do servidor', True)
            await message.channel.send('--> {}'.format(member.mention))
            await message.channel.send(embed=resposta)
        else:
            await message.channel.send('--> {} Não utilize comandos fora de {}'.format(member.mention, bot.mention))

#Launcher
client.run('token')
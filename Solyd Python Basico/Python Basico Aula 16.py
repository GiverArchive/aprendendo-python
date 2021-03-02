#Twitter
import oauth2
import pprint
import json
import urllib.parse

consumer_key = 'consumer key'
consumer_secret = 'consumer secret'

token_access = 'token access'
token_secret = 'token secret'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_access, token_secret)
twitter_client = oauth2.Client(consumer, token)

busca = input('O que deseja pesquisar no Twitter?\nR: ')
busca_adaptada = urllib.parse.quote(busca, safe='')
requisicao = twitter_client.request('https://api.twitter.com/1.1/search/tweets.json?q={}&lang=pt'.format(busca_adaptada))
decodificar = requisicao[1].decode()
objeto = json.loads(decodificar)
tweets = objeto['statuses']
for tweet in tweets:
    print(tweet['user']['screen_name'])
    print(tweet['text'])
    print("\n\n\n")

'''
post = 'Brasil'
post_encode = urllib.parse.quote(post, safe='')
postar = twitter_client.request('https://api.twitter.com/1.1/statuses/update.json?status={}'.format(post_encode), method="POST")
print(postar)
'''
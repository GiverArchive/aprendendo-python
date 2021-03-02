import json
import oauth2
import urllib.parse
import requests

class Twitter:

    def __init__(self, consumer_access, consumer_secret, token_access, token_secret):
        self.conexao(consumer_access, consumer_secret, token_access, token_secret)

    def conexao(self, consumer_access, consumer_secret, token_access, token_secret):

        self.consumer = oauth2.Consumer(consumer_access, consumer_secret)
        self.token = oauth2.Token(token_access, token_secret)
        self.twitter_client = oauth2.Client(self.consumer, self.token)
    
    def tweet(self, new):
        tweet_code = urllib.parse.quote(new, safe='')
        req = self.twitter_client.request('https://api.twitter.com/1.1/statuses/update.json?status={}'.format(tweet_code), method="POST")
        decodificar = req[1].decode()
        obj = json.loads(decodificar)
        return obj
    
    def search(self, query):
        requisicao = self.twitter_client.request('https://api.twitter.com/1.1/search/tweets.json?q={}&lang=pt'.format(urllib.parse.quote(query, safe='')))
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        tweets = objeto['statuses']
        return tweets
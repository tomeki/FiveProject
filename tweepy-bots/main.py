from credentials import *
import tweepy
from tweepy import OAuthHandler
import time

suffixes=["d’où?","d’où","d’où ?","d’où!","d’où !","d’ où?","d’ où","d’ où ?","d’ où!","d’ où !","d'où?","d'où","d'où ?","d'où!","d'où !","d' où?","d' où","d' où ?","d' où!","d' où !"]
suffixes2=["où?","où","où ?","où!","où !"]
global tweet_answered
tweet_answered = []

def init():

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(API_key,API_secret_key)
    auth.set_access_token(Access_token,Access_token_secret)
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    return api

def answer(tweet,msg,string):
    if "au cas où" in msg :
        print(f"ce message ne colle pas : {msg}")
        return False
    alreadyAnswered = False
    for tw in tweet_answered:
        if tw == tweet.user.screen_name:
            alreadyAnswered = True
    if alreadyAnswered == False:
        username = tweet.user.screen_name
        answer = "@"+username+ " "+string
        print(f"{msg}")
        print(f"{answer}")
        tweet = api.update_status(answer, tweet.id)
        tweet_answered.append(username)
        return True
    else:
        return False


api = init()
api.verify_credentials()
print("Authentication OK")
compteur_msg_send = 0
while(compteur_msg_send < 50):
    print("Looking for new tweets")
    for tweet in api.search(q="où",lang="fr",count=100):
        msg = str(tweet.text)
        if msg.endswith(tuple(suffixes)):
            if answer(tweet,msg,"De ton cul !"):
                compteur_msg_send += 1
                print(f"{compteur_msg_send}")

        elif msg.endswith(tuple(suffixes2)):
            if answer(tweet,msg,"Dans ton cul !"):
                compteur_msg_send += 1
                print(f"{compteur_msg_send}")
    time.sleep(10)



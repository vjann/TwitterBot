# Housekeeping: do not edit
import tweepy
import time
import random

auth = tweepy.OAuthHandler('tWBNCPcE9bRoyPgirSiYBJQCH', 'bKbmzMe0CqQ4l41j9zUzF6j813mJGwPXu07b3skzV3O9FuugjX')
auth.set_access_token('913509119730049031-LfE8miwRDyaVBpW0BV6QkH0xdNJ0SGu', '16CYXo6MiiBkzg2f8uESVgaPkmCb7hG2pPg1Q9lS350nI')
api = tweepy.API(auth)

user = api.get_user('LittyBits')
filename=open('genesis.txt')
f=filename.readlines()
num_lines = sum(1 for line in open('genesis.txt'))
filename.close()
# initially, the script will assume that the last tweet was a null value
# this is the function that does most of the work of the bot
if len(api.mentions_timeline()) > 0:
    lasttweet = api.mentions_timeline()[0]

# lastfollower = api.followers()

def runTime():
    # global lastfollower
    # flist = api.followers()
    # for i in range(0,len(flist)):
    #     if flist[len(flist)-i-1].id != lastfollower[len(lastfollower)-i-1].id:
    #         flist[i].follow()
    #         print (flist[i].screen_name)
    # lastfollower = flist
    #

    global lasttweet

    public_tweets = api.mentions_timeline()[0]

    search_results = public_tweets
    rid=search_results.id
    rsn=search_results.user.screen_name

    if public_tweets != lasttweet:
        happy = True
        m = "@%s " % (rsn)
        while happy:
            quote = random.choice(f)
            if len(quote) < 100:
                api.update_status(m + "Genesis " + quote, rid)
                happy = False
                print('tweeting')
        lasttweet = search_results

while True:
    runTime()
    print("sleeping")
    time.sleep(60)  # Sleep

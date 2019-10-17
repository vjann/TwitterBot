# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time

#enter the corresponding information from your Twitter application management:
CONSUMER_KEY = 'tWBNCPcE9bRoyPgirSiYBJQCH' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'bKbmzMe0CqQ4l41j9zUzF6j813mJGwPXu07b3skzV3O9FuugjX' #keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '913509119730049031-LfE8miwRDyaVBpW0BV6QkH0xdNJ0SGu' #keep the quotes, replace this with your access token
ACCESS_SECRET = '16CYXo6MiiBkzg2f8uESVgaPkmCb7hG2pPg1Q9lS350nI' #keep the quotes, replace this with your access token secret


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# access Twitter!
api = tweepy.API(auth)

# open our content file and read each line
filename=open('twitter.txt')
f=filename.readlines()
filename.close()

# for each line in our contents file, lets tweet that line out except when we hit a error
for line in f:
    try:
        api.update_status(line)
        print("Tweeting!")
    except tweepy.TweepError , err:
        print(err)
    time.sleep(1) #Tweet every 2 minutes
print("All done tweeting!")

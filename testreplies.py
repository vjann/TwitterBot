# Housekeeping: do not edit
import tweepy
import time

auth = tweepy.OAuthHandler('tWBNCPcE9bRoyPgirSiYBJQCH', 'bKbmzMe0CqQ4l41j9zUzF6j813mJGwPXu07b3skzV3O9FuugjX')
auth.set_access_token('913509119730049031-LfE8miwRDyaVBpW0BV6QkH0xdNJ0SGu', '16CYXo6MiiBkzg2f8uESVgaPkmCb7hG2pPg1Q9lS350nI')
api = tweepy.API(auth)

filename=open('twitter.txt')
f=filename.readlines()
filename.close()
# initially, the script will assume that the last tweet was a null value
lasttweet = api.user_timeline('vjannitor')[0]
# this is the function that does most of the work of the bot
def runTime():
    # uses the global lasttweet variable, rather than the local one
    global lasttweet

    # gets the most recent tweet by @ocertat and prints its id
    mostrecenttweet = api.user_timeline('vjannitor')[0]
    print(mostrecenttweet.id)

    # compares the two tweets, and tweets a line of Twain
    # if there is a new tweet from @ocertat
    if mostrecenttweet != lasttweet:
        if lasttweet.id%6 == 0:
            api.update_with_media('meme.png',"@vjannitor", in_reply_to_status_id = mostrecenttweet.id)
            print('tweeting')
            #api.update_status("@vjannitor nope", mostrecenttweet.id)
        elif lasttweet.id%6 ==1:
            api.update_status("@vjannitor " + f[0], mostrecenttweet.id)
            print('tweeting')
        elif lasttweet.id%6 ==2:
            api.update_status("@vjannitor " + f[1], mostrecenttweet.id)
            print('tweeting')
        elif lasttweet.id%6 ==3:
            api.update_status("@vjannitor " + f[2], mostrecenttweet.id)
            print('tweeting')
        elif lasttweet.id%6 ==4:
            api.update_status("@vjannitor " + f[3], mostrecenttweet.id)
            print('tweeting')
        elif lasttweet.id%6 ==5:
            api.update_status("@vjannitor " + f[4], mostrecenttweet.id)
            print('tweeting')
        lasttweet = mostrecenttweet


# runs the main function every 5 seconds
while True:
    runTime()
    print("sleeping")
    time.sleep(3)  # Sleep for 5 seconds

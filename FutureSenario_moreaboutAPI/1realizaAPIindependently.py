# In the tweepy doc, four important things are mentioned: authentication, cursor, extended tweets and streaming
# Instead of focusing on the user story a lot, this file is to realize the key methods in tweepy other than the streamer(we used it a lot in the main part)
# In the real world, we cannot have so much time to learn an API, or discuss about it
# The purpose is to find an efficient way to use the API, including in the future
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token = ''

#step1: get the access to the keys and secrets(authentication)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token)

api = tweepy.API(auth)

#step2: get the public tweets and the use the cursor

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
for status in tweepy.Cursor(api.user_timeline).items():
    # process status here
    process_status(status)
    
# step3: get the profile images


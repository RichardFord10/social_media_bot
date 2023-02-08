from config import *
from tweep import Twitter_Functions
from gpt import ChatGpt

hashtags = Twitter_Functions().get_trends()

while True:
   try:
      hashtag = random.choice(hashtags)
      Twitter_Functions().generate_random_trending_tweets()
      Twitter_Functions().like_and_follow_from_hashtag(hashtag, 10)
      Twitter_Functions().retweet_from_hashtag(hashtag, 10)
      time.sleep(350)
   except tweepy.errors.TweepyException as e:
      print(e)
      time.sleep(100)
      continue


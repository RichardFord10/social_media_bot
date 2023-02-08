from config import *
from tweep import Twitter_Functions
from gpt import ChatGpt

hashtags = Twitter_Functions().get_trends()


while True:
   try:
      Twitter_Functions().generate_random_trending_tweets()
      for hashtag in hashtags:
         Twitter_Functions().like_and_follow_from_hashtag(hashtag, 15)
      time.sleep(900)
   except tweepy.TweepError:
      time.sleep(100)
      continue


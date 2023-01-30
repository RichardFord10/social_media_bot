import tweepy
import keys
import oai as ai
import numpy as np

client = tweepy.Client(bearer_token=keys.twitter_bearer, consumer_key=keys.twitter_api_key, consumer_secret=keys.twitter_api_secret, access_token=keys.twitter_access_token, access_token_secret=keys.twitter_access_token_secret, wait_on_rate_limit=True)

class Twitter_Functions:
    
    def __init__(self):
        pass


    #Function to like a set number of tweets based on a single hashtag
    #@params hashtag: the hashtag to search, rate_limit: the amount of tweets to like, print_tweets: print the liked tweets to the terminal
    def like_tweet_from_hashtag(self, hashtag, rate_limit, print_tweets = True):
        query = '#'+str(hashtag)+' -is:retweet lang:en'
        tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=rate_limit)
        for tweet in tweets.data:
            if len(tweet.context_annotations) > 0:
                if(not print_tweets):
                    client.like(tweet.id)
                    print("Tweet with ID:"+str(tweet.id)+" liked")
                else:
                    print(tweet.context_annotations)
                    print("\n\n")
                    client.like(tweet.id)

    #Function to make a tweet
    #@params tweet_text: text of tweet, hashtag_array: an array of hashtags to include
    def make_tweet(self, tweet_text, hashtag_array = []):
        full_tweet = tweet_text + ' ' + ' '.join(["#" + tag for tag in hashtag_array])
        if(client.create_tweet(text=full_tweet)):
            print("Tweet "+full_tweet+" has been sent successfully!")
    

    #Function to retweet set number of tweets based on a single hashtag
    #@params hashtag: the hashtag to search, rate_limit: the amount of tweets to like, print_tweets: print the liked tweets to the terminal
    def retweet_from_hashtag(self, hashtag, rate_limit):
        query = '#'+str(hashtag)+' -is:retweet lang:en'
        tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=rate_limit)
        for tweet in tweets.data:
            if len(tweet.context_annotations) > 0:
                    client.retweet(tweet.id)
                    print("Tweet with ID:"+str(tweet.id)+" liked")
                    print(tweet.context_annotations)
                    print("\n\n")

    #Function to follow a set number of users based on a single hashtag
    #@params hashtag: the hashtag to search, rate_limit: the amount of tweets to like, print_tweets: print the liked tweets to the terminal
    def follow_from_hashtag(self, hashtag, rate_limit):
        query = '#'+str(hashtag)+' -is:retweet lang:en'
        tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'author_id'], max_results=rate_limit)
        for tweet in tweets.data:
            if len(tweet.context_annotations) > 0:
                    client.like(tweet.id)
                    client.follow_user(tweet.author_id)
                    print("User id: "+str(tweet.author_id)+" followed")
                    print(tweet.context_annotations)
                    print("\n\n")

    # Function to prompt user for multiple hashtags
    def prompt_for_hashtags(self):
        try:    
            hashtag_string = str(input("Enter the hashtags you would like to include, seperated by spaces: "))
            if(hashtag_string != False):
                hashtag_list = list(map(str, hashtag_string.split(' ')))
                hashtags = np.array(hashtag_list)
                return hashtags
        except ValueError():
            print("An Error has occured for hashtag prompt")

    # Function to prompt user for one hashtags
    def prompt_for_hashtag(self):
        try:    
            hashtag = str(input("Enter the hashtag you would like to utilize: "))
            if(hashtag != False):
                return hashtag
        except ValueError():
            print("An Error has occured for hashtag prompt")

    #Function to get all Follower IDS
    def get_all_follower_ids(self):
        ids = []
        followers = client.get_users_followers(keys.twitter_user_id)
        for info in followers.data:
            ids.append(info.id)
        return ids    

    #Function to get all Following IDS
    def get_all_following_ids(self):
        ids = []
        following = client.get_users_following(keys.twitter_user_id)
        for info in following.data:
            ids.append(info.id)
        return ids    
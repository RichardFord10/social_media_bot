import tweepy
import keys
import oai as ai
import numpy as np

client = tweepy.Client(bearer_token=keys.twitter_bearer, consumer_key=keys.twitter_api_key, consumer_secret=keys.twitter_api_secret, access_token=keys.twitter_access_token, access_token_secret=keys.twitter_access_token_secret, wait_on_rate_limit=True)

class Twitter_Functions:
    
    def __init__(self):
        pass

    project_url = r"https://github.com/RichardFord10/social_media_bot/"


    #Function to make a tweet
    #@params tweet_text: text of tweet, hashtag_array: an array of hashtags to include
    def _make_tweet(self, tweet_text, hashtag_array = []):
        full_tweet = tweet_text + ' ' + ' '.join(["#" + tag for tag in hashtag_array])
        if(client.create_tweet(text=full_tweet)):
            print("Tweet "+full_tweet+" has been sent successfully!")
    
    #Function to make a tweet
    def make_tweet():
        while True:
            try:
                include_source = str(input("Would you like to include the source code link? Y/N: "))
                tweet = str(input("Enter the text for the tweet you would like to create: "))
                if(tweet != False):
                    if(include_source.lower() == "y"):
                        source_text = " You can view my source code here --->" + project_url
                        if("#" in tweet):
                            self._make_tweet(tweet + source_text)
                        else:
                            hashtags = self.prompt_for_hashtags()
                            self._make_tweet(tweet + " You can view my source code here ------>", hashtags)
                    else:
                        if("#" in tweet):
                            self.make_tweet(tweet + source_text)
                        else:
                            hashtags = twitter_bot.prompt_for_hashtags()
                            self._make_tweet(tweet, hashtags)
            except ValueError:
                print("Error Occured")

    #Function to retweet set number of tweets based on a single hashtag
    #@params hashtag: the hashtag to search, rate_limit: the amount of tweets to like, print_tweets: print the liked tweets to the terminal
    def retweet_from_hashtag(self):
        hashtag = str(input("Enter the hashtag for the tweets you would like to search: "))
        limit = int(input("Enter a number under 100 "))
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
    def follow_from_hashtag(self):
        hashtag = self.prompt_for_hashtag()
        rate_limit = int(input("Enter a number under 100 "))
        query = '#'+str(hashtag)+' -is:retweet lang:en'
        tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'author_id'], max_results=rate_limit)
        for tweet in tweets.data:
            if len(tweet.context_annotations) > 0:
                    client.like(tweet.id)
                    client.follow_user(tweet.author_id)
                    print("User id: "+str(tweet.author_id)+" followed")
                    print(tweet.context_annotations)
                    print("\n\n")
    
    #Function to unfollow users 
    #@params hashtag: the hashtag to search, rate_limit: the amount of tweets to like, print_tweets: print the liked tweets to the terminal
    def unfollow_all_users(self):
        followers = self.get_all_following_ids()
        for follower in followers:
            client.unfollow_user(follower)

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

    #Function to like a set number of tweets based on a single hashtag
    #@params hashtag: the hashtag to search, rate_limit: the amount of tweets to like, print_tweets: print the liked tweets to the terminal
    def _like_tweet_from_hashtag(self, hashtag, rate_limit, print_tweets = True):
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

    #Function to like a set number of tweets based on a single hashtag
    def like_tweet_from_hashtag():
        hashtag = twitter_bot.prompt_for_hashtag()
        while True:
            limit = int(input("Enter a number between 1 & 100:  "))
            if(limit >= 1 and limit <= 100):
                break
            else:
                print("Incorrect Input, please enter a number between 1 and 100")
                continue
        try:
            print_tweets = str(input("Would you like to print the tweets being liked? Y/N: "))
            while print_tweets is not True or False:    
                if print_tweets.lower() == 'y':
                    print_tweets = True
                    break
                elif print_tweets.lower() == 'n':
                    print_tweets = False
                    break
                else:
                    print("Please enter either Y or N")
                    print_tweets = str(input("Would you like to print the tweets being liked? Y/N: "))
        except:
            print('Please Select a Valid Response')
            self._like_tweet_from_hashtag(hashtag, limit, print_tweets)
        


    # Function to prompt user to tweet out a prompt returned from the ChatGPT Class
    def prompt_for_gpt_tweet(self, prompt):
        send_tweet = str(input("Would you like to tweet the response? Y/N: "))
        while send_tweet is not True or False:    
            if send_tweet.lower() == 'y':
                send_tweet = True
                prefix = str(input("Do you want to type in a preface to this tweet?  Y/N: "))
                while prefix is not True or False:
                    if prefix.lower() == 'y':
                        prefix_text = str(input("Enter the preface: "))
                        prefix = True
                        break
                    elif prefix.lower() == 'n':
                        prefix = False
                        break
            elif send_tweet.lower() == 'n':
                        send_tweet = False
                        break
        if(send_tweet):
            hashtag = str(input("Do you want to add hashtags? Y/N: "))
            while hashtag is not True or False:
                if hashtag.lower() == 'y':
                    hashtag = True
                    hashtags = twitter_bot.prompt_for_hashtags()
                    break
                elif hashtag.lower() == 'n':
                    hashtag = False
                    break
            if(prefix):
                if(hashtag):
                    twitter_bot.make_tweet(prefix_text + "  " + gpt_prompt, hashtags)
                else:
                    twitter_bot.make_tweet(prefix_text + "  " + gpt_prompt)
            elif(hashtag):
                twitter_bot.make_tweet(gpt_prompt, hashtags)
            else:
                twitter_bot.make_tweet(gpt_prompt)
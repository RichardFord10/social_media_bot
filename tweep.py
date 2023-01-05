import tweepy
import keys
import geocoder

client = tweepy.Client(bearer_token=keys.bearer, consumer_key=keys.api_key, consumer_secret=keys.api_secret, access_token=keys.access_token, access_token_secret=keys.access_token_secret, wait_on_rate_limit=True)
project_url = r"https://github.com/RichardFord10/social_media_bot/blob/master/tweep.py"
class Twitter_Functions:
    
    #Function to like a set number of tweets based on a single hashtag
    #@params hashtag: the hashtag to search, rate_limit: the amount of tweets to like, print_tweets: print the liked tweets to the terminal
    def like_tweet_from_hashtag(self, hashtag, rate_limit, print_tweets = True):
        query = '#'+hashtag+' -is:retweet lang:en'
        tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=rate_limit)
        for tweet in tweets.data:
            if len(tweet.context_annotations) > 0:
                if(not print_tweets):
                    client.like(tweet.id)
                    print("Tweet with ID:"+str(tweet.id)+" liked")
                else:
                    print(tweet.context_annotations)
                    client.like(tweet.id)

    #Function to make a tweet
    #@params tweet_text: text of tweet, hashtag_array: an array of hashtags to include
    def make_tweet(self, tweet_text, hashtag_array = []):
        full_tweet = tweet_text + ' ' + ' '.join(["#" + tag for tag in hashtag_array])
        if(client.create_tweet(text=full_tweet)):
            print("Tweet "+full_tweet+" has been sent successfully!")
    

Twitter = Twitter_Functions()
# Twitter.like_tweet_from_hashtag("programming", 10, False)
Twitter.make_tweet("Consider following my account if youre interested in developement related things! You can view my source code here--> "+project_url, ['programming', 'developement', 'tweepy', 'twitterapi', 'python', 'github'])

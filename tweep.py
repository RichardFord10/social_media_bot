import tweepy
import keys
import geocoder

client = tweepy.Client(bearer_token=keys.bearer, consumer_key=keys.api_key, consumer_secret=keys.api_secret, access_token=keys.access_token, access_token_secret=keys.access_token_secret, wait_on_rate_limit=True)



class Tweet_Functions:

    def like_tweet_from_hashtag(self, hashtag, rate_limit):
        query = '#'+hashtag+' -is:retweet lang:en'
        tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=rate_limit)
        
        for tweet in tweets.data:
            print(tweet.text)
            if len(tweet.context_annotations) > 0:
                print(tweet.context_annotations)
                print('\n')
                print(tweet.id)
                client.like(tweet.id)
    
    
    def make_tweet(self, tweet_text, hashtags = []):
        hashtag = ["#" + tag for tag in hashtags]
        hashtag_string = ' '.join(hashtag)
        full_tweet = tweet_text + ' ' + hashtag_string
        if(client.create_tweet(text=full_tweet)):
            print("Tweet "+full_tweet+" has been sent successfully!")
    


Twitter = Tweet_Functions()
Twitter.make_tweet("This tweet is being sent from an automated script!", ['programming', 'python', 'tweepy', 'twitterapi'])
# Twitter.like_tweet_from_hashtag("learnprogramming", 10)

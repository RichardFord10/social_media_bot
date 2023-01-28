import tweep as twitter
import oai
import numpy as np

oai = oai.ChatGpt()
twitter_bot = twitter.Twitter_Functions()

while True:
    try:
        answer = int(input("Choose function: \n1: Like Tweet by Hashtag  \n2: Create a tweet  \n3: \n4: \n5:\n6: \n\n\n"))
        if answer == 1:
            hashtag = str(input("Enter the hashtag you want to like: "))
            while True:
                limit = int(input("Enter a number between 1 & 100: "))
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
            twitter_bot.like_tweet_from_hashtag(hashtag, limit, print_tweets)
            continue
        elif answer == 2:
            tweet = str(input("Enter the text for the hashtag you would like to create: "))
            if(tweet != False):
                if("#" in tweet):
                    twitter_bot.make_tweet(tweet)
                else:
                    hashtag_string = str(input("Enter the hashtags you would like to include, seperated by spaces"))
                    if(hashtag_string != False):
                        hashtag_list = list(map(str, hashtag_string.split(' ')))
                        hashtags = np.array(hashtag_list)
                        twitter_bot.make_tweet(tweet, hashtags)
            else:
                print("Error Occured")                        
            continue
        elif answer == 3:
            
            continue
        elif answer == 4:
            
            continue
        elif answer == 5:
            
            continue
        elif answer == 6:
            
            continue
        elif answer > 6 or answer <= 0:
            print("Please Enter a number from the menu above....\n")

    except ValueError:
        print("Error Occured\n")
        print("\n")
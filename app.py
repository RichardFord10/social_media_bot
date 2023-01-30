import tweep as twitter
import oai as openai
import numpy as np

ai = openai.ChatGpt()
twitter_bot = twitter.Twitter_Functions()
project_url = r"https://github.com/RichardFord10/social_media_bot/"

# Terminal Logic
while True:
    try:
        answer = int(input("Choose function: \n1: Like Tweet by Hashtag  \n2: Create a tweet  \n3: Rewtweet from hashtag \n4: Prompt ChatGPT and send tweet \n5: Follow users from hashtag \n6: \n\n\n"))
        if answer == 1:
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
            twitter_bot.like_tweet_from_hashtag(hashtag, limit, print_tweets)
            continue
        elif answer == 2:
            while True:
                try:
                    include_source = str(input("Would you like to include the source code link? Y/N: "))
                    tweet = str(input("Enter the text for the tweet you would like to create: "))
                    if(tweet != False):
                        if(include_source.lower() == "y"):
                            source_text = " You can view my source code here --->" + project_url
                            if("#" in tweet):
                                twitter_bot.make_tweet(tweet + source_text)
                            else:
                                hashtags = twitter_bot.prompt_for_hashtags()
                                twitter_bot.make_tweet(tweet + " You can view my source code here ------>", hashtags)
                        else:
                            if("#" in tweet):
                                twitter_bot.make_tweet(tweet + source_text)
                            else:
                                hashtags = twitter_bot.prompt_for_hashtags()
                                twitter_bot.make_tweet(tweet, hashtags)
                except ValueError:
                    print("Error Occured")                        
                continue
        elif answer == 3:
            hashtag = str(input("Enter the hashtag for the tweets you would like to search: "))
            limit = int(input("Enter a number under 100 "))
            twitter_bot.retweet_from_hashtag(hashtag, limit)
            continue
        elif answer == 4:
            prompt = str(input("Enter your prompt for Chat GPT: "))
            gpt_prompt = ai.prompt(prompt)
            print(gpt_prompt + "\n")
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
            else:
                continue
        elif answer == 5:
            hashtag = twitter_bot.prompt_for_hashtag()
            limit = int(input("Enter a number under 100 "))
            twitter_bot.follow_from_hashtag(hashtag, limit)
            continue
        elif answer == 6:
            continue
        elif answer > 6 or answer <= 0:
            print("Please Enter a number from the menu above....\n")
    except ValueError:
        print("Error Occured\n")
        print("\n")

import tweep as twitter
import oai as openai
import numpy as np

ai = openai.ChatGpt()
twitter_bot = twitter.Twitter_Functions()




# Terminal Logic
while True:
    try:
        answer = int(input("Choose function: \n1: Like Tweet by Hashtag  \n2: Create a tweet  \n3: Rewtweet from hashtag \n4: Prompt ChatGPT and send tweet \n5: Follow users from hashtag \n6: Unfollow all Following\n\n\n"))
        # Like Tweet by Hashtag
        if answer == 1:
            twitter_bot.like_tweet_from_hashtag()
            continue
        elif answer == 2:
            # Create a tweet
            twitter_bot.create_tweet()
            continue
        elif answer == 3:
            twitter_bot.retweet_from_hashtag()
            continue
        elif answer == 4:
            prompt = ai.prompt()
            twitter_bot.prompt_for_gpt_tweet(prompt)
        elif answer == 5:
            twitter_bot.follow_from_hashtag()
            continue
        elif answer == 6:
            twitter_bot.unfollow_all_users()
            continue
        elif answer > 6 or answer <= 0:
            print("Please Enter a number from the menu above....\n")
    except ValueError:
        print("Error Occured\n")
        print("\n")

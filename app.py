from config import *
from tweep import Twitter_Functions
from tts import Speech
from gpt import ChatGpt



while True:
    try:
        answer = int(input("Choose function: \n 1: Like Tweet by Hashtag  \n2: Create a tweet  \n3: Rewtweet from hashtag \n4: Prompt ChatGPT and send tweet \n5: Follow users from hashtag \n6: Unfollow all Following \n7: ttsgpt\n\n\n"))
        # L7
        # ike Tweet by Hashtag
        if answer == 1:
            Twitter_Functions.like_tweet_from_hashtag()
            continue
        elif answer == 2:
            # Create a tweet
            Twitter_Functions.make_tweet()
            continue
        elif answer == 3:
            Twitter_Functions.retweet_from_hashtag()
            continue
        elif answer == 4:
            prompt = ChatGpt.prompt()
            Twitter_Functions.prompt_for_gpt_tweet(prompt)
        elif answer == 5:
            Twitter_Functions.follow_from_hashtag()
            continue
        elif answer == 6:
            Twitter_Functions.unfollow_all_users()
        elif answer == 7:
            string = input("Enter a question: ")
            answer = ChatGpt.prompt(string)
            Speech.voicePlay(answer)
            continue
        elif answer > 7 or answer <= 0:
            print("Please Enter a number from the menu above....\n")
    except ValueError:
        print("Error Occured\n")
        print("\n")

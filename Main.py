import praw
import pandas as pd
import config
import tweepy
pd.set_option('max_colwidth', None)
reddit = praw.Reddit(client_id= config.CLIENT_ID, client_secret= config.CLIENT_SECRET, user_agent= config.USER_AGENT)
client = tweepy.Client( consumer_key=config.API_KEY, consumer_secret=config.API_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)
subs = reddit.subreddit('TwoSentenceHorror').top(time_filter ='day')
#filter out flair
for submission in subs:
    if submission.link_flair_text == "⭐ANNOUNCEMENT⭐":
        pass
    else:
        if submission.score > 500:
            response = client.create_tweet(text = submission.title + submission.selftext)

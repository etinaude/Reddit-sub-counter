import praw
import reddit_auth
'''
    please create a reddit script using this page https://old.reddit.com/prefs/apps/
    create a file named reddit_auth.py which contains the following class
    replace variables such as $ID with the details from the reddit script which was created.
    class secret:
        client_id = "$ID"
        client_secret = "$SECRET"
        user_agent = "my user agent"
    '''
reddit = praw.Reddit(client_id=reddit_auth.secret.client_id,
                     client_secret=reddit_auth.secret.client_secret,
                     user_agent=reddit_auth.secret.user_agent)
print(reddit.subreddit("UnleashSpace").subscribers)

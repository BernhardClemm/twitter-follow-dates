# Earliest possible following date of a Twitter follower

This repository provides a very simple function to provide some more information about when a Twitter user started following a certain account. The Twitter API (or web interface) does not provide the exact following date. 

However, Twitter sorts the list of followers according to following date, with the most recent follower on top - both on the platform and through the API `GET followers` endpoint ([see here - though this might change in future](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids)). The API also provides the date at which a user account was created. Therefore, the earliest possible following date of follower X is 
- the date at which an "earlier" follower's account was created, if this happened more recently than the creation of X's account or
- the date at which X's account was created otherwise.

The function assumes that the follower objects stored as Python dictionnaries in a list. With tweepy, the following code would produce such a list from the followers of my Twitter profile:

Setting up a Twitter API keys and session...
```
consumer_key="..."
consumer_secret="..."
    
access_token="..."
access_token_secret="..." 

twitter = OAuth1Service(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    base_url='https://api.twitter.com/1.1/')

session = twitter.get_session(token=[access_token,access_token_secret])

```
...setting up Tweepy...

```
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
```

... and storing all my followers into a list:

```
followers = []
for item in tweepy.Cursor(api.followers, screen_name="bernhardclemm").items():
    followers.append(item._json)
```
Now you can just run the function `following_dates()` like this:

```
following_dates(followers)
```
And you will find an dictionnary key called `followed_at_earliest` in each follower dictionnary. 

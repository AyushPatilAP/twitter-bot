import tweepy

auth = tweepy.OAuthHandler('SQbOlyESzrCXib77QDuK2mRr0','qYdyhQYcbRcwQVctj9lMM43flAgvf0Os1nsPhad9Ro8ViVEyNT')
auth.set_access_token('1132987858900344833-1Yp3cA6h8gpTG27Nb883AfpOonrQsT', 'mTdY0BLhb3RsumNuekJnhTEwjxX1ZQKWdmZfxiiIhsPYs')
user = api.me()

print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = ""#whatever you want to search
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
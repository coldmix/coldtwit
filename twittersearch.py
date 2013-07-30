#searching
def searchbyquery(api,query):
	tweets = []
	result = api.search(query)
	for ele in result:
		tweets.append(ele.text)
	return tweets

#get all tweets from  a users timeline
def searchusertimeline(api,username,count=100):
	timeline = api.user_timeline(screen_name=username, include_rts=True, count=count)
	tweets = []
	for tweet in timeline:
		tweets.append(tweet.text)
	return tweets


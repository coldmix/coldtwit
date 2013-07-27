#coldTwit
import tweepy

#CHANGE TO 'config.dat'
#USING LOCAL COPY WITH SENSITIVE INFO
config_path = 'config2.dat'

#parsing configuration details from config.dat
def parseConfigs():	
	reader = open(config_path)
	myarray = []
	for i in range(0,4):
		ele = reader.readline()
		ele = ele[ele.index("'")+1:-2]
		myarray.append(ele)
	reader.close()
	return myarray

#connect function which calls config and also returns the api
def connect():
	parray = parseConfigs()
	consumer_key=parray[0]
	consumer_secret=parray[1]
	access_token_key=parray[2]
	access_token_secret=parray[3]
	auth1 = tweepy.auth.OAuthHandler(consumer_key,consumer_secret)
	auth1.set_access_token(access_token_key,access_token_secret)
	api = tweepy.API(auth1)
	return api


if __name__ == '__main__':
    api = connect()
    user = 'narendramodi'
    timeline = api.user_timeline(screen_name=user, include_rts=True, count=100)
    for tweet in timeline:
    	print tweet.text

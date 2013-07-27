#coldTwit
import twitter

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
	api = twitter.Api(consumer_key,consumer_secret,access_token_key,access_token_secret)
	return api


if __name__ == '__main__':
    api = connect()
	print api.VerifyCredentials()

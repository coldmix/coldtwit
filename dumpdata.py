import getter
import unicodedata
import twittersearch
from time import gmtime, strftime


def dumpsearchdata():
	api = getter.connect()
	query = raw_input("Enter Search query: ")
	tweets = twittersearch.searchbyquery(api,query)
	print "Obtained ",len(tweets)," tweet(s)"
	fname = strftime("%Y-%m-%d.%H.%M.%S", gmtime())+query[:10]+'.tweets'
	print "Dumping to ",fname,"..."
	f = open(fname,"w")
	f.write('<tweet-data>\n')
	for ele in tweets:
		f.write('<tweet>\n')
		f.write(ele.encode('ascii','ignore')+'\n')
		f.write('</tweet>\n')
	f.write('</tweet-data>\n')
	print "Dumping complete"


if __name__ == '__main__':
	dumpsearchdata()
from TwitterAPI import TwitterAPI
import MySQLdb


consumer_key = 'W5lPcYK3EjoiO1peH4QYooC8l'
consumer_secret= 'ITiEUggIduJXpb1UCc3f12doS6TJkviXTNtrWcMLmQhZlt1Q1x'
access_key = '2719549261-Qtvgp9qqipEWPSnyueYN8p9fyNhPIFpga5AxFwR'
access_secret = 'Fto7aIUKYMMcaaFjj0DuTISQJQ802MBDSeuMazySDXzJm'

# connection = MySQLdb.connect("localhost","root","hitech123","mytweet")



def store_tweet(item):
	connection = MySQLdb.connect("localhost","root","hitech123","mytweet")
	cursor = connection.cursor()
	cursor.execute(" INSERT INTO tweets (tweet) VALUES (%s)", [item])
	connection.commit()


api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)

r = api.request('statuses/filter', {'track': "haircut"})

for item in r:
	if 'text' in item:
		try:
			#can be encode with UTF-8
			tw = (item['text']).encode('ascii', 'ignore')
			store_tweet(tw)
		except Exception as e:
			print 'hello buddy you hav an error'
	else:
		item
		


# for item in r:
# 	if 'text' in item:
# 		try:
# 			print item['text']
# 		except Exception as e:
# 			print(e)
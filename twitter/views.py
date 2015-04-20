from django.shortcuts import render
from django.http import HttpResponse
from .models import Haircut
from TwitterAPI import TwitterAPI

def fetch(request):
	try:
		get_data()
	except Exception, e:
		raise e
	finally:
		return HttpResponse("Ya it's Working You Can Check")

#Defineing all Access Keys
consumer_key = 'W5lPcYK3EjoiO1peH4QYooC8l'
consumer_secret= 'ITiEUggIduJXpb1UCc3f12doS6TJkviXTNtrWcMLmQhZlt1Q1x'
access_key = '2719549261-Qtvgp9qqipEWPSnyueYN8p9fyNhPIFpga5AxFwR'
access_secret = 'Fto7aIUKYMMcaaFjj0DuTISQJQ802MBDSeuMazySDXzJm'

#Procedure to Store tweets in DataBase
def get_data():
	api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)

	r = api.request('statuses/filter', {'track': "haircut"})

	for item in r:
		if 'text' in item:
			try:
				#can be encode with UTF-8 also
				tw = (item['text']).encode('ascii', 'ignore')
				Haircut.objects.create(tweet= tw)   #Insert Operation of DataBase
			except Exception as e:
				print 'hello buddy you hav an error during Insertion in DataBase'
		else:
			item

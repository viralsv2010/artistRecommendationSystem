# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:47:47 2014

@author: Feng Chen
"""

import twitter, sys, json
import time


reload(sys)
sys.setdefaultencoding("utf-8")

myApi=twitter.Api(consumer_key='4N4vCfC8priijLno5Bd3nAgGW', \
                  consumer_secret='idiRTR0kmkCZqMMusqSuKHZbsbKdZlQaqilK5Ze1tPxoByMGaQ', \
                  access_token_key='359839202-mUTxl4d50GZ6NQMT63X0TfVJlL9cBafbfozLcCky', \
                  access_token_secret='pyP7rdhAIUs3yCXQR7cUJ3TFrsFnXAH0jT56AqxMah4RQ')

def print_info(tweet):
    print '***************************'
    print 'Tweet ID: ', tweet['id']
    print 'Post Time: ', tweet['created_at']
    print 'User Name: ', tweet['user']['screen_name']
    try:
	    print 'Tweet Text: ', tweet['text']
    except:
		pass

def rest_query_ex3(i):
    query = 'concert OR vocalist OR musician OR singer OR band OR composer'
    i = str(i)
    geo = ('42.6525', '-73.7572', '150mi') # City of Albany
    tweets = myApi.GetSearch(query, geocode=geo, count = 100, result_type='recent')
    for tweet in tweets:
        print tweet.created_at, tweet.user.screen_name, tweet.text.encode("utf-8")
        output2 = {"id": tweet.id, "created_at": tweet.created_at, "screen_name": tweet.user.screen_name, "text": tweet.text}
        with open('api-data'+ i +'.txt', 'a+') as outputfile2:
            outputfile2.write(json.dumps(output2))
            outputfile2.write("\n")
    time.sleep(1000)

def main():
    """
        print "\n\n\n************ rest_query_ex1() ****************\n"
        rest_query_ex1()

        print "\n\n\n************ rest_query_ex2() ****************\n"
        rest_query_ex2()
    """
    i=0
    while True:
        print "\n\n\n************ rest_query_ex3() ****************\n"
        rest_query_ex3(i)
        i=i+1
        pass

if __name__ == '__main__':
    main()
"""
def rest_query_ex1():
    geo = ('40.730610', '-73.935242', '50mi')
    raw_tweets = myApi.GetSearch(term='music OR poem OR songs OR pop OR album OR genre OR melody OR track OR tune OR vocal', geocode=geo, count=100)
    for tweet in raw_tweets:
        print tweet.created_at, tweet.user.screen_name, tweet.text.encode("utf-8")
        output2 = {"created_at": tweet.created_at, "screen_name": tweet.user.screen_name, "text": tweet.text}
        with open('withlocation.txt', 'a+') as outputfile2:
            outputfile2.write(json.dumps(str(output2)))
            outputfile2.write("\n")


def rest_query_ex2():
    geo = ('40.730610', '-73.935242', '50mi') 
    raw_tweets = myApi.GetSearch(geocode=geo, count=100)
    for tweet in raw_tweets:
        print tweet.created_at, tweet.user.screen_name, tweet.text.encode("utf-8")
        output2 = {"created_at": tweet.created_at, "screen_name": tweet.user.screen_name, "text": tweet.text}
        with open('unbiased.txt', 'a+') as outputfile2:
            outputfile2.write(json.dumps(str(output2)))
            outputfile2.write("\n")
"""


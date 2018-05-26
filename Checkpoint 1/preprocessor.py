import os
import json
from pattern.en import positive, sentiment
import re
file_name = 'removedDuplicates.txt'
def task10():
    tweets = []
    # Reading each line and appending it to tweets array
    file10 = open('removedDuplicates.txt', 'r')
    file10Positive = open('preprocessed.txt', 'w')
    for line in file10:
        tweets.append(json.loads(line))

    for tweet in tweets:
        dataText = tweet['text']
        k = re.sub(r"http\S+", "", dataText)
        m = re.sub(r"[\\[\],.:;()\-&!]","",k)
        n = tweet['created_at']
        o = tweet['id']
        p = tweet['screen_name']


        file10Positive.write('{"text":' + json.dumps(m) + ', "created_at":' + json.dumps(n)+ 
        ', "id":' + json.dumps(o)+ ', "screen_name":' + json.dumps(p)+ "}" + '\n' )
    file10Positive.close()
if __name__ == '__main__':
    task10()
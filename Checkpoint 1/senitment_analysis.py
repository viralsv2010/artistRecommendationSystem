import os
import json
from pattern.en import positive, sentiment

file_name = 'removedDuplicates.txt'
def task10():
    print "Answer for Task 10"
    tweets = []
    # Reading each line and appending it to tweets array
    file10 = open('removedDuplicates.txt', 'r')
    for line in file10:
        tweets.append(json.loads(line))
        # Opening two files to add positive and negative tweets
    file10Positive = open('positive.txt', 'w')
    file10Negative = open('negative.txt', 'w')
    for tweet in tweets:
        # Finding Tweets Threshold value
        if positive(tweet['text'], threshold=0.1):
            # Writing Positive tweets to positive.txt
            print "Wonderful ... Its positive tweets."
            file10Positive.write(json.dumps(tweet) + '\n' )
        else:
            # Writing negative tweets to negative.txt
            print "Awful ... Negative tweets."
            file10Negative.write(json.dumps(tweet) + '\n')
    file10Positive.close()
    file10Negative.close()


if __name__ == '__main__':
    task10()
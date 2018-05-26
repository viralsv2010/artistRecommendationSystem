# import os
# import json
# from pattern.en import positive, sentiment

# file_name = 'api-data.txt'
# def task10():
#     print "Answer for Task 10"
#     tweets = []
#     tweeta = []
#     output = []
#     seen = set()
#     # Reading each line and appending it to tweets array
#     file10 = open('api-data.txt', 'r')
#     file10Positive = open('removedDuplicates.txt', 'w')
#     for line in file10:
#         tweets.append(json.loads(line))

#     for i in range(0, len(tweets)):
#         for x in range(i + 1, len(tweets)):
#             if tweets[i] == tweets[x]:
#                 flag = 1
#             else:
#                 flag = 0
#         if(flag == 0):
#             file10Positive.write(json.dumps(tweets[i]))
#             file10Positive.write(json.dumps('\n'))
#     # for tweet in tweets:
#     #     if tweet not in seen:
#     #         output.append(tweet)
#     #         seen.add(tweet)
#     #         file10Positive.write(json.dumps(tweet))
#     # print output
#     # for tweet in tweets:
#     #     # Finding Tweets Threshold value
#     #     print "tweet : ", tweet['text']
#     #     tweeta.append(tweet['text'])
        

# if __name__ == '__main__':
#     task10()


# Reference from http://www.codevscolor.com/2018/01/python-remove-duplicate-lines-text-file/
import hashlib
#removedDuplicates
output_file_path = "removedDuplicates.txt"
input_file_path = "api-data.txt"

completed_lines_hash = set()

output_file = open(output_file_path, "w")

for line in open(input_file_path, "r"):

  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file.close()
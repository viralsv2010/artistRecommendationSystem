import json
import csv
import re
"""
fileopen = open('api-data.txt','r')

data = json.load(fileopen)
print data[0]["text"]

with open('api-data.txt', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    print(distro['text'])
"""
data = {}
tweets = []
for line in open('preprocessed.txt', 'r'):
    tweets.append(json.loads(line))
with open('output.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['tweet_id','create_time','screen_name','username','text','matched','positive']) 
	for i in range(0,944):
		data=tweets[i]
		tweet_id = data['id']
		created_at = data['created_at']
		screen_name = data['screen_name']
		tweet_text = data['text']
		username = re.findall("@\w+", tweet_text)
		print tweet_id,created_at,screen_name,tweet_text
		matched = 'True'
		#newLine = '^'.join([str(tweet_id),created_at,screen_name,tweet_text,str(matched)])+'\n'
		spamwriter.writerow([str(tweet_id),created_at,screen_name,username,tweet_text,str(matched)])
	csvfile.close()



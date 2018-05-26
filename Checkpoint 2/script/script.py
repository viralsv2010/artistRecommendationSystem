import csv

with open('result.csv') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row:(row['support'],row['confidence']), reverse=False)


with open('sorted.csv', 'w') as f:
    fieldnames = ['support', 'confidence', 'rule']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in sortedlist:
        writer.writerow(row)






import hashlib
#removedDuplicates
output_file_path = "finaloutput.csv"
input_file_path = "sorted.csv"

completed_lines_hash = set()

output_file = open(output_file_path, "w")

for line in open(input_file_path, "r"):

  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file.close()
def isLineEmpty(line):
    return len(line.strip()) == 0

fb = open('output1.txt', 'w')
f = open('output.txt', 'r')
for index, line in enumerate(f.readlines()):
	if not isLineEmpty(line):
	    fb.write(line)
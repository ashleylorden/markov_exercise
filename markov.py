import random

def process_file(filename):
	dic = {}
	f = open(filename)
	contents = f.read()
	f.close()
	contents = contents.replace(".", ". ")
	contents = contents.replace("?", "? ")
	contents = contents.replace("!", "! ")
	line = contents.split()
	if line == []:
		pass
	else:
		n = len(line)
		for x in range(n-2):
			prefix = line[x], line[x+1]
			suffix = line[x+2]
			if dic.get(prefix) == None:
				dic[prefix] = [suffix]
			else:
				dic[prefix].append(suffix)
	return dic

def shift(t, n):
	return t[1], n

def build_sentence(dic):
	prefix = random.choice(dic.keys())
	suffix = random.choice(dic[prefix])
	words = [prefix[0], prefix[1], suffix]
	while words[-1][-1] not in "?.!":
		prefix = shift(prefix, suffix)
		suffix = random.choice(dic[prefix])
		words.append(suffix)	
	words = " ".join(words)
	return words.capitalize()	

def build_paragraph(dic, n):
	l = []
	for y in range(n):
		l.append(build_sentence(dic))
	return " ".join(l)

def build_tweet(dic):
	l = []
	counter = -1
	g = 0
	while True:
		l.append(build_sentence(dic))
		counter += 1
		for e in range(counter):
			g += len(l[e])
		if len(l[0]) > 140:
			l = []
		elif g > 140:
			l.pop()
			break	
	return " ".join(l)

def main():
	d = process_file("emma.txt")
	print build_sentence(d)
	print build_paragraph(d, 4)
	print build_tweet(d)


if __name__ == "__main__":
	main()
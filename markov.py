import random

def process_file(filename):
	dic = {}
	f = open(filename)
	contents = f.read()
	f.close()
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
		# if "?.!" in words and not words[-1][-1]:
			
	return " ".join(words)

def build_paragraph(dic, n):
	for y in range(n):
		build_sentence(dic)
	return "".join(build_sentence(dic))


def main():
	d = process_file("emma.txt")
	x = build_sentence(d)
	print x
	print build_paragraph(d, 4)

if __name__ == "__main__":
	main()
import random

def process_file(str):
	dic = {}
	f = open(str)
	line = f.readlines()
	if line == "":
		pass
	else:
		for len(line) n: #do this n-2 times, starting from 0 and adding 1 to start point each time
		line = line.split()
		pre1 = (line[0], line[1])
		suf1 = line[2]
		dic[pre1] = [suf1]
		if len(line) > 3:
			pre2 = (line[1], line[2])
			suf2 = line[3]
			dic[pre2] = [suf2]
	f.close()
	return dic

def shift(t, n):
	listy = list(t)
	o = listy[1], n
	return o

def build_sentence(dic):
	prefix = random.choice(dic.keys())
	suffix = dic[prefix]
	tup = (prefix[0], prefix[1], suffix[0])
	sentence = " ".join(tup)
	return sentence

def main():
	d = process_file("sample2.txt")
	x = build_sentence(d)
	print x
	# shift()


if __name__ == "__main__":
	main()
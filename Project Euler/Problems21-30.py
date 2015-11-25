import HelperFunctions as hf
from collections import Counter as mset

def problem21(n):
	sums = {}
	s = 0
	for i in range(1,n+1): sums[i] = sum(hf.properDivisors(i))
	for k,v in sums.iteritems():
		if k!=v and v in range(1,n+1):
			if sums[v] == k:
				s += k
	return s

def problem22():
	names = open('p022_names.txt','r').read().replace('"','').split(',')
	names.sort()
	letters={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
			'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
			'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
	total = 0
	for i in range(len(names)):
		name = names[i]
		score = 0
		for l in name: score += letters[l]
		score *= (i+1)
		total += score
	return total

def problem23():
	abundant = []
	s = 0
	for i in range(1,28124):
		j = sum(hf.properDivisors(i))
		if j>i: abundant.append(i)
	additive = set([])
	for a in abundant:
		for b in abundant:
			additive.add(a+b)
	for i in range(28124):
		if i not in additive: s += i
	return s

def problem24():
	i = 1
	n = '0123456789'
	nextLexo(n)

def nextLexo(n):
	l = len(n)
	if n[-1]>n[-2]

def main():
#	print 'Problem 21 %s' % problem21(10000)
#	print 'Problem 22 %s' % problem22()
#	print 'Problem 23 %s' % problem23()
	print 'Problem 24 %s' % problem24()
#	print 'Problem 15 %s' % problem15x3(20)
#	print 'Problem 16 %s' % problem16(1000)
#	print 'Problem 17 %s' % problem17()
#	print 'Problem 18 %s' % problem18()
#	print 'Problem 19 %s' % problem19()
#	print 'Problem 20 %s' % problem20(100)

if __name__ == '__main__':
	main()

import HelperFunctions as hf
from collections import Counter as mset

def problem1():
	sum = 0
	for i in range(1000):
		if i%3==0 or i%5==0:
			sum += i
	return sum

def problem2():
	fib1 = 1
	fib2 = 2
	interim = 0
	total = 0
	while fib1 < 4000000:
		if fib1%2==0:
			total += fib1
		interim = fib1+fib2
		fib1 = fib2
		fib2 = interim
	return total

def problem3():
	m = 600851475143
	i = 1
	while i<m:
		if m%i==0:
			m /= i
		i += 1
	return m

def problem4():
	biggest = 0
	for i in range(100,1000):
		for j in range(100,1000):
			if hf.isPalindrome(i*j):
				if i*j > biggest:
					biggest = i*j
	return biggest

def problem5():
	factors = mset()
	for i in range(21):
		pf = mset(hf.primeFactorization(i))
		a = pf - factors
		factors += a
	b = list(factors.elements())
	return reduce(lambda x,y: x*y, b)

def problem6():
	sum = reduce(lambda x,y: x+y, range(101))
	sqosum = sum**2
	sumosq = reduce(lambda x,y: x+y**2, range(101))
	return sqosum-sumosq

def problem7():
	counter = 0
	i = 1
	while counter < 10001:
		i += 1
		if hf.isPrime(i):
			counter += 1
	return i

def problem8():
	prod = 0
	num = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"
	for i in range(len(num)-13):
		seg = num[i:i+13]
		n = reduce(lambda x,y: int(x)*int(y), list(seg))
		if n > prod:
			prod = n
	return prod

def problem9():
	n = 1000
	z = [i**2 for i in range(1,n)]
	for a in z:
		for b in z:
			if b>a:
				if b+a in z:
					if b**.5 + a**.5 + (b+a)**.5 == n:
						return (a**.5)*(b**.5)*((b+a)**.5)

def problem10():
	sum = 0
	for i in range(2,2000000):
		if hf.isPrime(i):
			sum += i
	return sum

def main():
	print 'Problem 1 %s' % problem1()
	print 'Problem 2 %s' % problem2()
	print 'Problem 3 %s' % problem3()
	print 'Problem 4 %s' % problem4()
	print 'Problem 5 %s' % problem5()
	print 'Problem 6 %s' % problem6()
#	print 'Problem 7 %s' % problem7()	#Not efficient (fixed prime calc SLIGHTLY.  Haven't retested)
	print 'Problem 8 %s' % problem8()
#	print 'Problem 9 %s' % problem9()	#Not bad, but slow(ish)
#	print 'Problem 10 %s' % problem10()	#Not terribly eficient

if __name__ == '__main__':
	main()
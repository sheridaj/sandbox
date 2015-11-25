import math

def isPalindrome(num):
	p = str(num)
	while len(p) > 1:
		a = p[0]
		b = p[-1]
		if a != b:
			return False
		p = p[1:-1]
	return True

def primeFactorization(num):
	factors = []
	a = num
	i = 2
	while a>1:
		if a%i==0:
			factors.append(i)
			a /= i
			i = 2
		else:
			i += 1
	return factors

def isPrime(num):
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
	return True

def divisors(num):
#	THIS IS WRONG
	factors = primeFactorization(num)
	print factors
	divisors = set([1,num])
	for f in factors:
		while f < num:
			divisors.add(f)
			f = f**2
	return divisors

def properDivisors(num):
	divisors = [1]
	for i in range(2,int(math.ceil(math.sqrt(num)+1))):
		if num%i == 0 and i!=num: divisors+=[i,num/i]
	return set(divisors)
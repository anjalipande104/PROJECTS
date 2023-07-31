import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

# return appropriate N that satisfies the error bounds
def findN(eps,m):
	return int(2*(m/eps)*(math.log(26,2))*(math.log((2*(m/eps))*(math.log(26,2)),2)))
	#let p be pattern and l be substring different than p such that
	# (Σ(26**m-i-1)pi)%q = (Σ(26**m-i-1)li)%q
	# So,((Σ(26**m-i-1)(pi-li))%q=0
	#so , q can give false values of when it is prime factor of the term (Σ(26**m-i-1)(pi-li)
	# so as per the formula given in assignment ,
	# the no. of prime factor of any no. a is equal or less than to log|a|
	# the no. of primes less than or equal to π(N) ≥ N / (2 log2 N)
	# let N be the upper bound prime no. 
	# so the probability of l being false +ve is no. , e =< (2m(logN)log26)/N......(e=eps)
	# N/logN => log(2mlog26/e).......1
	# taking log on both side in 1 logN-log(logN) => log(2mlog26/e)..........2
	# by multiplying 1 and 2 we get ; N-(Nlog(logN)/logN) => (2mlog26/e)(log(2mlog26/e))
	# as log(logN)/logN will lia between 0 and 1/2
	# so on solving, therefore N will be greater than and equal to (2mlog26/e)log(2mlog26/e)

#this will compute 26 to the power m-1,where m =lenth of patern
def power_find(q,m):
    h=1
    for i in range(m-1):
        h = (h*26) % q
    return h

# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
    h=0
    m=len(p)
    n=len(x)
    h=power_find(q,m)
    a=0
    b=0
    L=[]
    v=0
    
# This will give hash value,a = hash value of pattern p and b = hash value of first m character of x
    for i in range(m):
        v=power_find(q,m-i)
        a=(v*((ord(p[i])-ord('A'))%q)+a)%q
        b=(v*((ord(x[i])-ord('A'))%q)+b)%q
    
# this will check the hash value is same or not ,
    for i in range(n-m+1):
# this will check , if the hash value is same as pattern , if yes then append it in list L     
        if (a)==(b):
            L.append(i)
        
# if i is less then n-m , then it will delect the value of ith index of x and add (i+m)th index of x
        if i < n-m:
            b=(((26*(b-((ord(x[i])-ord('A'))*h)%q))%q)+(ord(x[i+m])-ord('A'))%q)
# if b is less than zero , it will add q
            if b < 0:
                b = b+q
        
    return L
    
def modPatternMatchWildcard(q,p,x):
    h=0
    m=len(p)
    n=len(x)
    h=power_find(q,m)
    a=0
    b=0
    L=[]
    r=0
    v=0
    # This will give hash value,a = hash value of pattern p and b = hash value of first m character of x leaving the value of index where wildcard entry is
    for i in range(m):
        if p[i]!='?':
            v=power_find(q,m-i)
            a=((v*(ord(p[i])-ord('A')))%q+a)%q
            b=((v*(ord(x[i])-ord('A')))%q+b)%q
        else:
            r=i
    # this v is eqal to 26 to the power m-r-1 
    v=power_find(q,m-r)
    # this g is eqal to 26 to the power m-r-2
    g=power_find(q,m-r-1)
    # this will check , if the hash value is same as pattern , if yes then append it in list L 
    for i in range(n-m+1):
        if (a)==(b):
            L.append(i)
                
        if i < n-m:
            b=((26*(b-(h*(ord(x[i])-ord('A')))+(v*(ord(x[i+r])-ord('A')))-(g*(ord(x[i+r+1])-ord('A')))))+(ord(x[i+m])-ord('A')))%q    
            if b < 0:
                b = b+q
                
    return L
    
  
    
        
    
    
    
    
    
    
    
    
    
    
    
    


    
    
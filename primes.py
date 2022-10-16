def primeFinder():

	lowLimit = int(input("Inclusive lower limit --> "))
	upLimit = int(input("Inclusive upper limit --> "))
	print("")

	primes = []

	i = lowLimit

	while i <= upLimit:
		s = []
		k = 1
		while k <= i:
			if (i % k) == 0:
				s.append(k)
			k += 1
		if len(s) == 2:
			primes.append(i)
		elif i == 1:
			primes.append(i)
		i += 1

	print(primes)

def antiPrime():
	upLimit = int(input("Inclusive upper limit --> "))
	print("")

	antiPrimes = []

	factors = [0]

	i = 1

	while i <= upLimit:
		s = []
		k = 1
		while k <= i:
			if (i % k) == 0:
				s.append(k)
			k += 1
		factors.append(len(s))
		hits = []
		x = 0
		while x <= i:
			if factors[x] >= factors[i]:
				hits.append(x)
			x += 1
		if len(hits) == 1:
			antiPrimes.append(i)
		i += 1
	print(antiPrimes)

def factorization():
	y = 1

	while y <= 1:
		y = int(input("Enter a number greater than 1 to factorize --> "))
		print("")

	primes = []

	i = 1

	while i <= y:
		s = []
		k = 1
		while k <= i:
			if (i % k) == 0:
				s.append(k)
			k += 1
		if len(s) == 2:
			primes.append(i)
		i += 1

	factor = []
	fProd = 1
	x = 0
	slide = y
	while fProd != y:
		hit = primes[x]
		if slide%hit == 0:
			factor.append(hit)
			slide = slide/hit
			fProd = fProd * hit
		else:
			x += 1
	
	print(factor)

def calcLoop():
	print("")
	actionStep = raw_input("Find `prime` numbers, `antiprime` numbers or `factorize` a number --> ")
	print("")
	actionStep = actionStep.lower()

	if actionStep == "prime":
		primeFinder()
		calcLoop()
	elif actionStep == "antiprime":
		antiPrime()
		calcLoop()
	elif actionStep == "factorize":
		factorization()
		calcLoop()
	else:
		calcLoop()

calcLoop()


import math




def prime(num):
	for i in range(2,round(math.sqrt(num))):
		print(num%i)
		if num%i == 0:
			return False
	return True

for i in range(2,100):
	if prime(i):
		print(i)
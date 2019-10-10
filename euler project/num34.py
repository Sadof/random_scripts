def fact(num):
	prod = 1
	for i in range(2,num+1):
		prod *= i
	return prod

def num34():
	count = 0
	for i in range(3,10000000):
		sum = 0
		for num in str(i):
			sum += fact(int(num))
		if sum == int(i):
			count += int(i)
			print(i)


num34()
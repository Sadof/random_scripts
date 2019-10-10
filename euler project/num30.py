from Decorators import timer


@timer
def num30():
	s = 0
	for i in range(2,200000):
		if i == sum([int(j)**5 for j in str(i)]):
			s += i
			print(i)
	print("Sum: ",s)
num30()
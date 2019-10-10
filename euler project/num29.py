from Decorators import timer


@timer
def num29(a,b):
	int_set = set()
	for i in range(2,a+1):
		for j in range(i,b+1):
			int_set.add(i**j)
			int_set.add(j**i)
	return int_set

int_set = num29(100,100)
print(len(int_set),int_set)
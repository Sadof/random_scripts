from Decorators import timer



def num32():
	product_set = set()
	arr= []
	num_set = set()
	for i in range(1,100):
		for j in range(100,10000):
			if i*j > 9999:
				break
			for n in str(i):
				num_set.add(int(n))
			for n in str(j):
				num_set.add(int(n))
			for n in str(i*j):
				num_set.add(int(n))
			if len(num_set) == 9 and 0 not in num_set:
				product_set.add(i*j)
				arr.append(i,j)
				print(i,j,i*j)
			
			num_set.clear()
	return product_set

print(sum(num32()))



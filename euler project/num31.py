from Decorators import timer




def num31(coin_pos,coin_sum):
	coin_value = [100,50,20,10,5,2,1]
	count = 0

	if coin_sum <= 200:
		coin_sum += coin_value[coin_pos]
		print(coin_sum)
		num31(coin_pos+1 if coin_pos !=0 else coin_pos,coin_sum)
	else:
		if coin_sum == 200:
			count += 1
		num31(coin_pos-1,coin_sum-coin_value[coin_pos-1]-coin_value[coin_pos])

num31(0,0)
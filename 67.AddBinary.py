from typing import List
from itertools import zip_longest
class Solution:
	def algo(self, a, b):
		a = a[::-1]
		b = b[::-1]
		
		aux = '0'
		sol = ''
		for x,y in zip_longest(a, b, fillvalue='0'):
			if x == '1' and y == '1':
				if aux == '1':
					sol = '1' + sol 
					aux = '1'
				else:
					sol = '0' + sol 
					aux = '1'  
			elif x == '0' and y == '0':
				if aux == '1':
					sol = '1' + sol 
					aux = '0'
				else:
					sol = '0' + sol 
					aux = '0'
			else:
				if aux == '1':
					sol =  '0' + sol 
					aux = '1'
				else:
					sol = '1' + sol 
					aux = '0'
		if aux == '1':
			sol = '1' + sol
		
		return sol




if __name__ == "__main__": 
	a = "000100"
	b = "110010"
	x = Solution().algo(a,b)
	print(x)
 
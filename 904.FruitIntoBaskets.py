from typing import List
from collections import defaultdict

class Solution:
	def totalFruit(self, fruits: List[int]) -> int:
		dic = defaultdict(int)
		max = 0

		last_bask = ''
		last_acumulate = 0
		for i,fruit in enumerate(fruits):		
			dic[fruit] += 1
			
			if len(dic) > 2:
				value = sum(dic.values()) - 1
				if (value > max):
					max = value
				
				aux = list(dic.keys())
				aux.remove(fruits[i])
				aux.remove(fruits[i-1])
				del dic[aux[0]]

				dic[fruits[i-1]] = last_acumulate
			
			if last_bask != fruit:
				last_bask = fruit
				last_acumulate = 1
			else:
				last_acumulate += 1

		value = sum(dic.values())
		if (value > max):
			max = value
		
		return max
		


if __name__ == "__main__": 
	fruits = [1,2,3,2,2]
	x = Solution().totalFruit(fruits)
	print(x)

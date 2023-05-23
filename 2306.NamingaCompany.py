from collections import defaultdict
from typing import List

class distinctNames:
	def distinctNames(self, ideas: List[str]) -> int:
		dic = defaultdict(set)
		for idea in ideas:
			prefix_idea = idea[:1]
			base_idea = idea[1:]
			dic[base_idea].add(prefix_idea)
		
		sol = 0
		for x in range(len(ideas) - 1):
			for y in range(x + 1, len(ideas)):
				baseA,baseB = ideas[x][1:], ideas[y][1:]
				prefixA,prefixB = ideas[x][0], ideas[y][0]
				
				if prefixB not in dic[baseA] and prefixA not in dic[baseB]:
					sol += 1
		
		return sol * 2
			
				



if __name__ == "__main__": 
	ideas = ["coffee","donuts","time","toffee"]
	sol = distinctNames().distinctNames(ideas)
	print(sol)


from typing import List

def isValid(s: str) -> bool:
	stack = []
	
	for x in s:
		if x in ('(','{','['):
			stack.append(x)

		if x == ')':
			if stack.pop() != '(':  
				return False
		if x == '}':
			if stack.pop() != '{':
				return False
		if x == ']':
			if stack.pop() != '[':
				return False  
	return True


if __name__ == "__main__": 
	isValid('(((())))')

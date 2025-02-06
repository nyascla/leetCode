'''
Problema
    Dos jugadores A y B
    Pieldras en fila
    cada piedra tiene un valor
    conseguir la maxima puntuacion
Restricciones
    Cada turno se puede coger 1,2 o 3 piedras

Solucion
MinMaxPattern
diferencia A - B o B - A 
'''
from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def dfs(alice, i):
            if i >= len(stoneValue):
                return 0

            res = float("-inf")
            valor = 0
            for x in range(1, 3 + 1):
                if i + x - 1 >= len(stoneValue):
                    break

                valor += stoneValue[i + x - 1]
                if alice:
                    res = max(res, valor + dfs(not alice, i + x))
                else:
                    res = min(res, dfs(not alice, i + x) - valor)
            print(alice, i, res)
            return res

        value = dfs(True, 0)
        print(value)
        res = ''
        if value == 0:
            res = 'Tie'
        elif value > 0:
            res = 'Alice'
        else:
            res = 'Bob'

        return res

if __name__ == "__main__":
    piles = [2, 7, 9, 4, 4]
    sol = Solution().stoneGameIII(piles)

'''
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

Array
Math
Dynamic Programming
Game Theory
'''
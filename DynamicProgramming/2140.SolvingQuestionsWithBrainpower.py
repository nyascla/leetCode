from typing import List
'''
FUERZA BRUTA
    solucion recursiva 
    nodo hoja devolvemos 0 
    si no dos opciones
    saltar o tomar devolvemos el mayor valor estre las dos opciones
        def dp(i):
            # Si salimos del arbol estamos en una hoja
            if i >= len(questions):
                return 0  # eso no suma
            salto = questions[i][1]
            valor = questions[i][0]

            # llamadas a nodos hijos
            return max(dp(i + 1), dp(i + 1 + salto) + valor)

        return dp(0)

PROGRAMACION DINAMICA
    - subproblemas
    que es mayor coger el valor y tomar la penalizacion o saltar el valor y tomar el valor de la siguiente pregunta
    Si tomamos estas decisiones de derecha a izquierda la solucion optima es trivial porque ya conocemos el futuro de cada decision
    la solucion consiste en almacenas en un array de derecha a izquierda el valor optimo
    la ultima posicion siempre sera el valor de esa pregunta
    la primea posicion siempre sera la maximo de puntos
    
    - subproblema optimo
    siempre podemos saber el valor obtimo para cada subproblema
    skip + valor de la casilla siguente ??? take + valor de la casilla donde se ha saltado
'''
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dp(i):
            if i >= len(questions):
                return 0  # eso no suma
            if i in dt:
                return dt[i]

            salto = questions[i][1] + 1
            valor = questions[i][0]

            dt[i] = max(dp(i + 1), valor + dp(i + salto))

            return dt[i]

        dt = {}
        return dp(0)



if __name__ == "__main__":
    #questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    sol = Solution().mostPoints(questions)
    print(sol)

'''
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.
'''
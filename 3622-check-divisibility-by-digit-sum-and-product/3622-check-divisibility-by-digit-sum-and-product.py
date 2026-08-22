class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n = str(n)
        summation = 0
        multiply = 1

        for i in range(len(n)):
            summation += int(n[i])
            multiply *= int(n[i])

        n = int(n)

        return n % (summation + multiply) == 0
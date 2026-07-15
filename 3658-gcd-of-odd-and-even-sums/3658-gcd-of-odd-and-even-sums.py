class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        Even = []
        Odd = []
        
        i = 1

        while(len(Even) < n and len(Odd) < n):
            if i % 2 == 0:
                Even.append(i)
            else:
                Odd.append(i)
        sumEven = sum(Even)
        sumOdd = sum(Odd)
        ans = math.gcd(sumEven, sumOdd)

        return ans


        
            

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for i in range(low, high + 1):
            num = str(i)

            if len(num) % 2 != 0:
                continue

            summation1 = 0
            summation2 = 0

            for j in range(len(num) // 2):
                summation1 += int(num[j])

            for k in range(len(num) // 2, len(num)):
                summation2 += int(num[k])

            if summation1 == summation2:
                count += 1

        return count
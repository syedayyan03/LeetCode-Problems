class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        diff = 0
        left_q = 0
        right_q = 0

        for i in range(n):
            if num[i] == '?':
                if i < n // 2:
                    left_q += 1
                else:
                    right_q += 1
            else:
                digit = int(num[i])

                if i < n // 2:
                    diff += digit
                else:
                    diff -= digit

        if (left_q + right_q) % 2 == 1:
            return True

        return diff != (right_q - left_q) // 2 * 9
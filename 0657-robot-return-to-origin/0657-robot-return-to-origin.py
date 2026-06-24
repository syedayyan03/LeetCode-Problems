class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # x = 0
        # y = 0

        # for i in range(len(moves)):
        #     if moves[i] == 'U':
        #         y += 1
        #     elif moves[i] == 'D':
        #         y -= 1
        #     elif moves[i] == 'L':
        #         x -= 1
        #     elif moves[i] == 'R':
        #         x += 1

        # return x == 0 and y == 0

        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
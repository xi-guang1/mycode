from math import ceil

class Solution:
    def minimumMoves(self, s: str) -> int:
        a = s.split("O")
        res = 0
        for i in a:
            num = 0
            for j in i:
                if j == "X":
                    num += 1
            res += ceil(num / 3)
        return res
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        total = 0
        for i in jewels:
            total+= stones.count(i)
        return total
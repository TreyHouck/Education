class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(x in jewels for x in stones)
        
        ##So the way I understand this one, is that we are using a list to find the number of combinations in jewels before then searching for those jewl combinations in stones.
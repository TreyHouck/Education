class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for X in operations:
            if X[1] == "+":
                x += 1
            else: 
                x -= 1
        return x
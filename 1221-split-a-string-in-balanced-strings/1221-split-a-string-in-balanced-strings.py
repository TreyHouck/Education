class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(accumulate(1 if x == "R" else -1 for x in s)).count(0)

#set a flag to zero and loop through characters in string;
#if char is R, add flag by 1; if char is L, subtract 1 from flag;
#add 1 to counter whenever flag is 0.
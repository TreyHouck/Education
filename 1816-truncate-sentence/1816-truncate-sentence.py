class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        wordlist=s.split(" ")
        truncated_list=wordlist[:k]
        s = " ".join(truncated_list)
        return s

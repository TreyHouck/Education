class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
      return max(len(x.split(" ")) for x in sentences)

      #This returns the max number of items in x, divided into groups by quotation marks, for x in sentences
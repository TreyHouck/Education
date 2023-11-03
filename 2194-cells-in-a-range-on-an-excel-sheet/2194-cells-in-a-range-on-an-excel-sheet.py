class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        start_letter, start_num = start[0], int(start[-1])
        end_letter, end_num = end[0], int(end[1])
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        alphabet_slice = \
            alphabet[alphabet.index(start_letter):alphabet.index(end_letter) + 1]
        res = list()
        for el in alphabet_slice:
            res += [el + str(num) for num in range(start_num, end_num + 1)]
        return res

        #This program starts by splitting string s into two lists, start and end.  It then defines the variables for start/end letter/numbers of each cell. With this, we then first find the range of the indexed value between the two alphabetical letters (plus one because it doesn't include the last value). We then create a list for our result wherein we add num as a string where we use range to return the lisut of numbers between the two cells. 
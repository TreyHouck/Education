class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d={}
        ans= ""

        n = 0 
        for i in key:
            if i not in d and i != " ":
                d[i]=chr(ord('a')+n)
                n += 1
        
        for i in message:
            if i in d:
                ans += d[i]
            elif i == " ":
                ans += " "
        
        return ans

        #This code creates a dictionary d that maps each unique character in key (excluding whitespace) to a lowercase letter of the alphabet (starting from 'a'). It then iterates through each character in message, and if the character is in the dictionary d, it appends the corresponding letter to a string ans. If the character is a whitespace, it appends a whitespace to the string ans. The final string ans is then returned
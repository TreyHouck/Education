class Solution:
    def interpret(self, command: str) -> str:
       return command.replace('()','o').replace('(al)','al')

       #Takeaway: Commands can be chained with periods
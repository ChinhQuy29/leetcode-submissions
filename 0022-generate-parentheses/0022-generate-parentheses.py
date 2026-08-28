class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s):
            balance = 0
            for c in s:
                balance += 1 if c == "(" else -1

                if balance < 0:
                    return False
                
            return not balance
        
        res = []

        def backtrack(s):
            if len(s) == n * 2:
                if valid(s):
                    res.append(s)
                return 
            
            backtrack(s + "(")
            backtrack(s + ")")
            
        backtrack("")
        return res
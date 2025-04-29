class Solution:
    def clearDigits(self, s: str) -> str:
        num = '1234567890'
        l = []
        for i in s:
            if i in num:
                l.pop()
            else:
                l.append(i)
        
        return ''.join(l)
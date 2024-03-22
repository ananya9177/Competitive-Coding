class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for op in tokens:
            if op=='+':
                a,b=s.pop(),s.pop()
                s.append(b+a)
            elif op=='-':
                a,b=s.pop(),s.pop()
                s.append(b-a)
            elif op=='*':
                a,b=s.pop(),s.pop()
                s.append(b*a)
            elif op=='/':
                a,b=s.pop(),s.pop()
                s.append(int(b/a))
            else:
                s.append(int(op))
        return s.pop()

        

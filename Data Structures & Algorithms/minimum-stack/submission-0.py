class MinStack:

    def __init__(self):
        self.stack=[]
        self.topi=-1

    def push(self, val: int) -> None:
        self.topi+=1
        self.stack.append(val)
        return

    def pop(self) -> None:
        if self.topi==-1:
            pass
        else:
            self.topi=self.topi-1
            self.stack.pop()
        return 

    def top(self) -> int:
        return self.stack[self.topi]

    def getMin(self) -> int:
        mini=self.stack[0]
        for x in self.stack:
            if x<mini:
                mini=x
        return mini

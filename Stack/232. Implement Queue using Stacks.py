class MyQueue:

    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if self.out_stack == []:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            
        return self.out_stack[-1]
    

    def empty(self) -> bool:
        return self.in_stack == [] and self.out_stack == []

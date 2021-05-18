class Stack:

    def __init__(self, n):
        self.top = -1
        self.stack = [0] * n

    def my_push(self, item):

        if self.top < len(self.stack)-1:
            self.top += 1
            self.stack[self.top] = item
        else:
            print('스택이 꽉 차있다.')

    def my_pop(self):

        if self.top < 0:
            print('스택이 비어있다.')
        else:
            last = self.stack.pop(self.top)
            self.top -= 1

        return last

    def my_is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def __str__(self):
        return str(self.stack)


stack = Stack(3)
stack.my_push(1)
stack.my_push(2)
stack.my_push(3)
print(stack)
print(stack.my_pop())
print(stack)
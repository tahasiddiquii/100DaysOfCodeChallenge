class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Cannot peek an empty stack.")

    def size(self):
        return len(self.items)


# Example usage:
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Stack size:", my_stack.size())  # Output: 3
print("Top element:", my_stack.peek())  # Output: 30

popped_item = my_stack.pop()
print("Popped item:", popped_item)  # Output: 30
print("Stack size after pop:", my_stack.size())  # Output: 2

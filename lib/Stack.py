class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if len(self.items)>0 :
            top = self.items[len(self.items)-1]
            self.items.pop()
            return top

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items)==self.limit

    def search(self, target):
        stack_len = len(self.items)
        for i in range(stack_len):
            if self.items[i] == target:
                return stack_len - i - 1

        return -1


    
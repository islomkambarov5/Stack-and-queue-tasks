class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    # Stack: Push for Stack
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    # Stack: Pop for Stack
    def pop(self):
        if not self.top:
            return None
        dummy = self.top
        self.top = self.top.next
        dummy.next = None
        self.height -= 1
        return dummy.value

    def print_list(self):
        temp = self.top
        lst = []
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        return lst

    # Stack: Implement Stack
    def stack(self):
        stack_list = Stack(None)
        print('success')
        return stack_list

    # Stack: Parentheses Balanced
    def is_balanced_parenthes(self, string):
        if string:
            stack = Stack(string[0])
        else:
            return False
        need0 = 0

        for symbol in string:
            if symbol == "(":
                stack.push(symbol)
                need0 += 1
            elif symbol == ")":
                if stack.pop() == "(" and ")" not in stack.print_list():
                    return False
                need0 -= 1
                stack.pop()
            else:
                return False

        if not need0:
            return True
        else:
            return False

    # Stack: Reverse String
    def reverse_str(self, string: str):
        return string[::-1]

    # Stack: Sort Stack
    def sort_stack(self):
        sorted_stack = Stack()

        while not self.is_empty():
            temp = self.pop()

            while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
                self.push(sorted_stack.pop())

            sorted_stack.push(temp)

        while not sorted_stack.is_empty():
            self.push(sorted_stack.pop())


# Queue Using Stacks: Enqueue - i didn't understood

class Queue:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.front = new_node
            self.rear = new_node
            self.size = 1
        else:
            self.front = None
            self.rear = None
            self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def is_empty(self):
        return self.front is None

    def pop(self):
        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return temp.value

    def print_list(self):
        temp = self.front
        lst = []
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        return lst

    # Queue Using Stacks: Dequeue
    def dequeue(self):
        if self.is_empty():
            return None
        return self.pop()


MyStack = Stack(1)
MyQueue = Queue(1)
from random import randint

rand_list = []

for i in range(10):
    random_num = randint(1, 10)
    MyStack.push(random_num)
    rand_list.append(random_num)

MyStack.sort_stack()
print(MyStack.print_list())
print(rand_list)

for i in range(10):
    MyQueue.append(i)
print(MyQueue.print_list())
MyQueue.dequeue()
print(MyQueue.print_list())

# MyStack.stack()
# print(MyStack.is_balanced_parenthes("()(()"))

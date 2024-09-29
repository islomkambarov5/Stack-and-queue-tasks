Stack: Implement Stack Using a List ( ** Interview Question)
In the Stack: Intro video we discussed how stacks are commonly implemented using a list instead of a linked list.

Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.

___
Stack: Push for Stack That Uses List ( ** Interview Question)
Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.

Remember: This Stack implementation uses a list instead of a linked list.

---
Stack: Pop for Stack That Uses List ( ** Interview Question)
Add a method to pop a value from the Stack implementation that we began in the last two Coding Exercises.

Remember: This Stack implementation uses a list instead of a linked list.

---
Stack: Parentheses Balanced ( ** Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.  Indent all the way to the left.



This will use the Stack class we created in these coding exercises:

---
Stack: Reverse String ( ** Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.

This will use the Stack class we created in the last three coding exercises:

---
Stack: Sort Stack ( ** Interview Question)
The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 

The function should use the pop, push, peek, and is_empty methods of the Stack object.

Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.

This will use the Stack class we created in these coding exercises:



The function should perform the following tasks:

Create a new instance of the Stack class called sorted_stack.

While the input stack is not empty, perform the following:

Pop the top element from the input stack and store it in a variable temp.

While the sorted_stack is not empty and its top element is greater than temp, pop the top element from sorted_stack and push it back onto the input stack.

Push the temp variable onto the sorted_stack.

Once the input stack is empty, transfer the elements back from sorted_stack to the input stack. To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it onto the input stack.



You can also click on "Hints" (above) to see the pseudo-code.

Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original stack, due to the nested loops used to compare the elements.  However, the function should only use one additional stack, which could be useful in situations where memory is limited.

---
Queue Using Stacks: Enqueue ( ** Interview Question)
You are given a class MyQueue which implements a queue using two stacks. Your task is to implement the enqueue method which should add an element to the back of the queue.

To achieve this, you can use the two stacks stack1 and stack2. Initially, all elements are stored in stack1 and stack2 is empty. In order to add an element to the back of the queue, you need to first transfer all elements from stack1 to stack2 using a loop that pops each element from stack1 and pushes it onto stack2.

Once all elements have been transferred to stack2, push the new element onto stack1. Finally, transfer all elements from stack2 back to stack1 in the same way as before, so that the queue maintains its ordering.

Your implementation should satisfy the following constraints:



The method signature should be def enqueue(self, value).

The method should add the element value to the back of the queue.

---
Queue Using Stacks: Dequeue ( ** Interview Question)
You have been tasked with implementing a queue data structure using two stacks in Python, and you need to write the dequeue method.

The dequeue method should remove and return the first element in the queue.
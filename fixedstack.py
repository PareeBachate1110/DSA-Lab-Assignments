class Node:
    def __init__(self, data):
        self.data = data            #current data
        self.next = None            #next node is unknown, hence assigned to "None"
      

class Stack:
    def __init__(self):
        self.top = None         #currently stack is empty hence topmost element is "None"
        self.count=0            #there are 0 elements in the stack rn
        self.maxno=5            #stack can have maximum size 5

    def isEmpty(self):
        return self.count==0        #returns boolean value

    def isFull(self):
        return self.count==self.maxno   #returns boolean value

    def push(self, data):
        if self.isFull():
            print("Stack Overflow")
        else:
            new_node = Node(data)               #will be added to "data" in Node class
            new_node.next = self.top            #make the new node's next point to the current top node.
            self.top = new_node                 #Make the new node the new top.
            self.count += 1
            print(f"{data} pushed into stack")

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            popped = self.top.data              #get the data from the top node
            self.top = self.top.next            #move top to the next node, removing the current top
            self.count -= 1
            print(popped, "popped from stack")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element is:", self.top.data)

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack:", end=" ")

            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()


stack = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element: "))
        stack.push(element)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")

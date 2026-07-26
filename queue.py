class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)
        print(item,"added to Queue.")

    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty. Cannot dequeue.")
        else:
            removed=self.queue.pop(0)
            print(removed,"removed from the queue.")

    def peek(self):
        if len(self.queue)==0:
            print("Queue is Empty.")
        else:
            print("Front Element is:",self.queue[0])

    def display(self):
        if len(self.queue)==0:
            print("Queue is empty.")
        else:
            print("Queue:",self.queue)

q=Queue()
while True:
    choice=int(input("1. Enqueue 2. Dequeue 3. Peek 4. Display\nEnter Choice:"))
    if choice==1:
        item=input("Enter element:")
        q.enqueue(item)
    elif choice==2:
        q.dequeue()
    elif choice==3:
        q.peek()
    elif choice==4:
        q.display()
    else:
        print("Please Enter a Valid Number.")
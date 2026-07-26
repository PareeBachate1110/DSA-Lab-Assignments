stack=[]
def push():
    data=input("Enter Data:")
    stack.append(data)

def pop():
    print("Popped Item Is:",stack.pop(-1))

def peek():
    print("Top Item Is:",stack[-1])

def display():
    print("All Elements Are As Follows:\n",stack)

while True:
    ch=int(input("1 for Push, 2 for Pop, 3 for Peek, 4 for Displaying All Elements \nEnter Choice:"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    elif ch==4:
        display()
    else:
        print("Please Enter a Valid Number.")
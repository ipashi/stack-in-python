top = -1 # variable to point the topmost element
size =5 # size of the stack
stack = [0]*size # initializing the list with all zeros
# inserting elements to stack
def push(data):
	global top # referencing to global top variable
	temp = top 
	temp+=1 #increment the top before inserting element
	if(size<=temp):
		print("Stack is full")
	else:
		stack[temp]=data
		top+=1
push(1) # insert 1 to stack
push(2) # insert 2 to stack
push(3) # insert 3 to stack
push(4) # insert 4 to stack
push(5) # insert 5 to stack
push(6) # output stack is full as stack reached its size 
# popping elements from stack 
def pop():
	global top 
	if(top==-1):
		return "stack is empty"
	else:
		temp = top
		top-=1 #decrement the top before inserting element 
		return stack[temp]
print(pop()) #pops out 5 from stack
print(pop()) #pops out 4 from stack
print(pop()) #pops out 3 from stack
print(pop()) #pops out 2 from stack
print(pop()) #pops out 1 from stack
print(pop()) #returns stack is empty
# checking stack is empty or not
def isEmpty():
	global top 
	if(top==-1):
		return True
	else:
		return False
print(isEmpty())
# returns the topmost elements from the stack
def peek():
	global top 
	if(top==-1):
		return "stack is empty"
	else:
		return stack[top]
print(peek())

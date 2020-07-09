# importing reduce function
from functools import reduce 
# The main function of the code
def factorial(x):
    ValueofX = x
    # in this list are stored all the numbers between 1 and the input
    mylist = []
    for i in range(1,x):
        # everytime the loop runs the value of x decreases and it is stored in mylist 
        mylist.append(x)
        x = x - 1
    # here I use the reduce function to multiply all the members of the list
    fact = reduce((lambda x,y: x*y),mylist)
    print("The factorial of %d is %d" % (ValueofX,fact))
# The code runs continously until the window is closed
while True:
    UserInput = int(input("Enter an integer: "))
    factorial(UserInput)
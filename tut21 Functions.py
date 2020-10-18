# a=123
# b=321
# c= sum((a,b)) #Built In Function
# print(c)
#
def function1():
    print("Hello You Are in Function 1")

function1()


# def function1(a,b):
#     print("Hello You Are in Function 1", a+b)
#
# function1(24,6)

def func2(a,b):
    """This Function Calculate Average of Two Numbers"""
    average = (a+b)/2
    print(average)     #Ye print hta v dunga to koi problem nhi hoga
    return average

# Function se kuch na kuch Return Zarur kre

variable1= func2(12,6)
print(variable1)

print(func2.__doc__)
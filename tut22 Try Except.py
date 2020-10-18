# num1= input('Enter Num 1\n')
# num2= input('Enter Num 2\n') # Agar koi user Alphabet daal diya to error dega
#
#
# try:
#     print("The Sum of these two numbers is",
#             int(num1)+int(num2))
# except Exception as e:
#     print(e)

#Error Throw nhi krega Bs Error Ko Likh dega
#Or Baki Niche Program ko Execute Karega

print("This Line Is Very Important... Copyright Adi all rights...")

num1= input('Enter Num 1\n')
num2= input('Enter Num 2\n') # Agar koi user Alphabet daal diya to error dega


try:
    print("The Sum of these two numbers is",
            int(num1)+int(num2))
except:
      print("Unable To calculate Please Enter Number Only")



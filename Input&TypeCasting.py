a = int(input('Enter you age: ')) # if I  just used input() function , then it did take my input as string
print("Your age is:",a , "and it's :", type(a))

b = str(a)
c = float(b)
print("The value of b is :", b, "and it's :", type(b))
print("The value of c is :", c, "and it's :", type(c))

name = input("Enter Your Name: ")
print(name, ",", "Is It You!"," ","This is a :", type(name))

num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
print('The type of num1 is: ', type(num1))
print('The type of num2 is :', type(num2))
sum = int(num1) + int(num2) # sum = int(num1 + num2), it means concatenate of those two given strings, not addition
print('The sum of num1 and num2 is :', sum, ", And the type of sum is:", type(sum))
# print(num1 + num2 + 4) , 
# if I run it, it'll through an error, because here num1 and num2 are taken as strings and 4 is an integer. defferent data types can't be added together.

# below are the examples of how to add strings and integers together:
print("Concatenate1 of strings:",num1 + num2 + '4') 
print("Concatenate2 of strings:",num1 + num2 + str(4))
print("Addition of integer numbers :",int(num1) + int(num2) + 4) 
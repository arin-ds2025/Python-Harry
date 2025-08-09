'''
REPL --> Read Evaluate Print Loop
This module provides a simple REPL for evaluating python expressions
Basically a terminal session that allows you to enter python code , so it(terminal) can be called REPL
'''

#Arithmetic Operators
'''
1. Addition (+)
2. Subtraction (-)
3.Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Floor Division (//)
7. Exponentiation (**)
'''
a=32
b=5
print("a // b is :", a//b) # Floor Division is basically division that returns the largest integer less than or equal to the result. it basically removes the decimal part of the result
print("2 ** 3 is :", 2**3) # Exponentiation is the operation of raising one number to the power of another
print("21 % 4 is :", 21%4) # Modulus is the operation that finds the remainder of division of one number by another
print(" ")


#Comparison Operators ( it always returns a boolean value(True/False) )
'''
1. Equal to (==)
2. Not equal to (!=)
3. Greater than (>)
4. Less than (<)
5. Greater than or equal to (>=)
6. Less than or equal to (<=)
 '''
print("1 == 1.0 : ", 1==1.0)
print("5 > 5.0012 : ", 5>5.0012)
print(" ")


# Logical Operators (it returns a boolean value(True/False) based on the logical operation performed)
'''
1. and 
2. or
3. not
4. xor (exclusive or)
5. nand (not and)
6. nor (not or)
7. xnor (not exclusive or)
8. implies (if...then)
'''
# implies mean if the first condition is true then the second condition must also be true
A = True
B = False
implies_result = (not A) or B
print(implies_result,'\n')  # False
#in another way
def implies(a, b):
    return (not a) or b
print(implies(True, True))   # True
print(implies(True, False))  # False
print(implies(False, True))  # True
print(implies(False, False)) # True
print(" ")


# Assignment Operators 
'''
1. Simple assignment (=)
2. Add and assgin (+=)
3. Subtract and assign (-=)
4. Multiply and assign (*=)
5. Divide and assign (/=)
6. Modulus and assign (%=)
7. Floor divide and assign (//=)
8. Exponentiate and assign (**=)
'''
a=4
a **= 2
print("a**= 2 is : ", a)
print(" ")


# Membership Operators (it checks if a value is present in a sequence or not)
'''
1. in
2. not in
'''
print('5.0012 is not 5.0012 : ',5.0012 is not 5.0012)
print("5 in [1,2,3,4,5.0] : ", 5 in [1,2,3,4,5.5])
print(" ")

# Identity Operators (it checks if two variables point to the same object in memory)
'''
1. is
2. is not
'''
print('5 is 5.0 : ', 5 is 5.0)
print("5.01 is not 5.011 : ", 5.01 is not 5.011)
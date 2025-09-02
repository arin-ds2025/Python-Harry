# for loop
fact = 1
limit = int(input("Enter the factorial limit: "))
for i in range(1,limit+1):
    if i == limit:
        print(i,end=" = ")
        fact *= i
        break
    else:
        print(i, end="*")
        fact *= i
print(fact," ","Factorial of ",limit)
print(' ')

table = int(input("Enter the table number:"))
for i in range(1,11):
    print(f"{table} X {i} = {table*i}")
print(" ")

for i in range(1,21):
    if i == 18:
        break
    if i%2 == 0:
        continue
    print(i) # it will print odd numbers only from 1 to 20 for the continue statement, except 19 for the break statement

# while loop
height = int(input("Enter the height of the pyramid: "))
i = 1
while i <= height:
    print("     " * (height-i) + " <*> " * (2*i-1)) 
    i+=1
    '''
    here, " "*(height-i) is used to print leading spaces to center the pyramid
    and " * "*(2*i-1) is used to print the stars in each row.  
    The number of stars or anything else in each row is (2*i-1) which is always odd
    '''
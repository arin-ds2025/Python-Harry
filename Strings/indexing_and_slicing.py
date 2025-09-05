# Strings are immutable,it means we can't change the characters of a string

name = 'Arin'
#name[2] = 'y' # it will give an error because strings are immutable
print(name[0:]) # it will print the whole string
print(name[::-1]) # it will print the string in reverse order with negative indexing using slicing 

email = 'arin2023b@gmail.com'
print('the index number of @ is :', email.index('@')) # .index() method will return the index number of a character in a string
print('Your username is: ',email[:email.index('@')])
print(" ")

fullname = "Arin Ahmed"
print("The length of the fullname is: ",len(fullname))
for i in range(len(fullname)):
    print(i," : ",fullname[i])
print(" ")

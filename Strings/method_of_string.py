name = 'assaba tarannum'
print("Upper case of the name: ",name.upper())
print("Lower case of the name: ",name.lower())
print("Title of the name: ",name.title()) # in each word, first letter will be capitalized
print("Capitalize of the name: ",name.capitalize()) # only the first letter of the first word will be capitalized
print(" ")
name1 = '   assaba tarannum   '
print("strip of name1 :",name1.strip()) # removes any leading (spaces at the beginning) and trailing (spaces at th end) characters
print("right strip of name1 :",name1.rstrip()) # removes any trailing characters (spaces at the end)
print("left strip of name1 :",name1.lstrip()) # removes any leading characters (spaces at the beginning)
print(" ")
intro = "She is Assaba Tarannum (Saba)"
print("find of the intro: ",intro.find('Saba')) # returns the nth index of the string
# find() and index() are similar but if the string is not found, find() returns -1 while index() raises an error
print("index of the intro: ",intro.index('Saba'))
print("Replace Tarannum from the intro with Tabassum: ",intro.replace('Tarannum','Tabassum'))
print(" ")
print("Split the intro: ",intro.split()) # splits the string into a list
intro1 = "She is Assaba Tarannum (Saba)"
print("Split the intro with , : ",intro1.split("Assaba")) # splits the string into a list with 'Assaba' as a separator
print(" ")
print("Check if the intro starts with 'She' : ",intro.startswith('She'))
print("Check if the intro ends with 'Haga' : ",intro.endswith('Haga'))
print(" ")
fname = 'Arin'
join_name = '-'.join(fname) # join() method takes all items in an iterable and joins them into one string
print("Join the fname and lname with 'Rebuker Op': ",join_name)
# split() and join() are inverse of each other
# where, split() method splits a string into a list and join() method joins a list into a string
fruits = "Apple,Banana,Mango"
print(fruits.split(','))
print(",".join(['Apple','Banana','Mango']))
print(" ")
learn='Python311'
print("Check if all characters in learn are alphanumeric: ",learn.isalnum())
print("Check if all characters in learn are alphabetic: ",learn.isalpha())
print("Check if all characters in learn are digits: ",learn.isdigit())
print("Check if all characters in learn have spaces: ",learn.isspace())
print("Check if all characters in learn are lowercase: ",learn.islower())
print("Check if all characters in learn are uppercase: ",learn.isupper())
print("Check if all characters in learn are titlecase: ",learn.istitle())
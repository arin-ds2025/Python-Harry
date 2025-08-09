# this is a single line commnet
'''
this is a 
multi-line commnet

'''

# Excape sequence characters: (mainly use \)

print("Hello mc,\n How are doing today? \t LoL") # \n for new line, \t for tab space
# if I've to use single \ in my string then I need to use double \\ in my string
print("This is a backslash: \\ \n this is next line \t (this is tab space)")
#if I need to use double or single quote in my string then I need to use \ before it
print('This is single quote: \' ')
print('This is double quote: \" ')
print(" ")
print("This Is single quote: (\') \t this is double quote: (\") ")
print(" ")
# but in double quotes I can user single quote without escape sequence and also in single quotes I can user double quote without escape sequence
print('This is double quote: " \n') # here \n use extra new line and it can be used instead of using print(" ")
print("this is single quoteL ' ")
print(" ")
print("Hello","world","This","is",'Arin', sep='/') # sep is used to separate the strings with the given character in sep=''
print('hello world', end='..') # end is used to end the string with the given character in end='' but by default it is end='\n' so that it goes to next line
print('This is Arin',sep=' ', end='@Data Science Engineer',) # but end="" doesn't use space in between the strings so we need to use sep=" " 
# if I use end="!\n" then it will end the string with ! and go to next line 

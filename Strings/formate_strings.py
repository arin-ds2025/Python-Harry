template = "Hello, {}. You Got CGPA {} out of 4.0"
n1 = "Arin"
cg1 = 3.67
n2 = "Shihab"
cg2 = 3.20
n3 ='Nayem'
cg3 = 3.10

s1 = template.format(n1, cg1)
s2 = template.format(n2, cg2)
s3 = template.format(n3, cg3)
print(s1)
print(s2)
print(s3)
print(" ")

# or
print(f"Hello, {n1}. You Got CGPA {cg1} out of 4.0")
print(f"Hello, {n2}. You Got CGPA {cg2} out of 4.0")
print(f"Hello, {n3}. You Got CGPA {cg3} out of 4.0")
print(" ")

# to get ascii value of a character : ord() function is used
print('ASCII value of d :',ord('d'))

# to get character from an ascii value : chr() function is used
print('69 is the ASCII value of character :',chr(69))
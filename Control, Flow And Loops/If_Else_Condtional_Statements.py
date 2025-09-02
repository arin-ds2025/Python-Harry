def get_valid_cgpa():
    try:
        user_input = input("Enter Your CGPA in floating number (between 1.0 and 4.0): ")
        cgpa = float(user_input)
        if not (1.0 <= cgpa <= 4.0):
            raise ValueError("CGPA must be between 1.0 and 4.0")
        
        if '.' in user_input:
            parts = user_input.split('.')
            if len(parts[1]) != 1 or len(parts) != 2 :
                raise ValueError("CGPA must have exactly one decimal point")
        else:
            cgpa = float(user_input + '.0')    
        
        print(f"Valid CGPA entered: {cgpa}")
        return cgpa                  

    except ValueError as e:
        print(f"Invalid input: {e}. Please try again and give a valid CGPA..!")
        return None
    
CGPA = get_valid_cgpa()    

if CGPA is None:
    print("Terminating program due to invalid CGPA input.")
    exit()
     
if CGPA >= 3.5 and CGPA <= 4.0:
    print("Excellent Result..!")
    if CGPA == 4.0:
        print("Congratulations, You have achieved the highest CGPA..!")
    else:
        print("Keep it up, you can do better")
elif CGPA >= 3.2 and CGPA < 3.5:
    print("Good Result..!")
    print("You Have to Work Hard to get Excellent Result")
elif CGPA >=3.0 and CGPA <3.2:
    print("Average Result..!")
    print("You have to work hard to get better result..!")
elif CGPA >=2.5 and CGPA < 3.0:
    print("Pass but It's a below average result..!")
    print("You have to work very hard to do better..!")
else:
    print("Fail..!")
    print('You have to work very hard to get a better result..!')



    
    
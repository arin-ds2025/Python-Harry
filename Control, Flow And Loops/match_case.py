# it's kind of similar to swtich case statement

roll = int(input("Enter Your roll number: "))

if(roll >= 700000 and roll < 800000):
    print("Valid Roll Number..!")
    if((roll == 758571 or roll ==  758572 or roll ==  758574 or roll ==  758578)):
        print("Data Found..!")
    else:
        print("Data Not Found..!")
else:
    print("Invalid Roll Number..!")
    exit()

match roll:
    case 758572:
        print("Hey Arin, What's up..!")
    case 758571:
        print("Hey Murad, Mara khaa")
    case 758574:
        print("hey Shihab, Kuggee")
    case 758578:
        print("Hey Nayem, Confirm fail..!")
    case roll if roll == 700000 or roll == 799999:
        print("Allaaah Huakbar..!")
    case _:  # _ means default case
        print("Agge")
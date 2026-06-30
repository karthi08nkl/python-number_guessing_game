import random

def game(attempts=None):
    num = 0
    comp = random.randint(1,100)
    i = 0
    won = False
    while attempts is None or i < attempts:
        try:
            num = int(input("Enter a Number from 1-100 : "))
        except ValueError:
            print("Please enter a valid integer!")
            continue

        if num < 1 or num > 100:
            print("Number must be between 1 and 100!")
            continue
        i+=1 
        if(num<comp):
            print("LOW!\n")
        elif(num>comp):
            print("HIGH!\n")
        else:
            print("CORRECT!\n\n")
            won = True
            break
       
    if(attempts is None or i<attempts):
        print(f"You took {i} attempts to find !") 

    if won:   
        print("You Won the Game")  
    else:
        print("You Lose the Game")   

    print(f"Computer chose {comp}")     

print("NUMBER GUESSING GAME\n")
print("Rules")
print("There are 3 Modes :")
print("1.EASY (Unlimited Attempts)")
print("2.MODERATE (10 Attempts)")
print("3.HARD (5 Attempts)")
print("Enter any one MODE (1/2/3)\n")
choice = int(input("Enter your Choice :"))

match choice:
    case 1:
        game()
    case 2:
        game(10)
    case 3:
        game(5)   
    case _:
        print("Invalid Choice")    
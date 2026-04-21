greeting = input("What is your name: ")
print("\nHello", greeting, "Can you answer this question.\n" )

score = 0




ask_1 = input(" Yes/ No: Is python excute line by line: ")
if ask_1 == "yes":
    score += 1
    print("Correct! Your score is ", score)
else:
    
    print("Wrong answer, your score is ",score)

print("\nwhich of the following is correct" )
print("A) Python is a framwork ")
print("B) Python python is a low level language")
print("C) python is compile programing language ")
print("D) Python is an interpreter programing language\n")

print("'Note'If you miss this Question You Can Get one more change\n")

ask_2 = input ("The correct answer is A/B/C/D: " )

if ask_2.lower() == "d":
    score += 1
    print("Correct! Your score is ", score)
elif ask_2.lower() != "d":
    ask_2_wrong = input("Yes/No: Can i change the question for you as chance: ")
    if ask_2_wrong.lower() == "yes":
        second_chance = input("\nName any two python libraries no More/less than two: ").split()
        if len(second_chance) == 2:
            score += 1
            print("Correct! Your score is ", score)
        else:
            print("You missed it ")

    else:
        print("Thank you")

else:
    
    print("Wrong answer! Your Score is ", score)

ask_3 = input("\nTrue/False: Python Uses identation: ")
if ask_3.lower()  == "true":
    score += 1
    print("Correct! Your score is ", score)
else:
   
    print("Wrong answer! Your Score is ", score)

ask_4 = input("\nYes/No: in python you Can create a fuction without using 'def' keyword: ")
if ask_4.lower() == "no":
    score += 1
    print("Correct! Your score is ", score)
else:
    
    print("Wrong answer! Your Score is ", score)

ask_5 = input("\nTrue/False:  Python is a friendly to learn: ")
if ask_5.lower() == "true":
    score += 1
    print("Correct! Your score is ", score)
else:
    
    print("Wrong answer! Your Score is ", score)
total = score
print("This is the End of question\n\nYour Tatal Score is: ", score, "out of 5")

exit()
import time
i = 1
name = input("Enter your name: \n")
oppo = input("Enter opponents name: \n")
user_score = 0
comp_score = 0
import random
rounds = int(input("How many rounds do you want to play? \n"))
while i<rounds+1:

    time.sleep(1)
    user = input("Enter your choice\nRock\nPaper\nScissors\n")

    comp = random.choice(["Rock","Paper","Scissors"])

    if user == "Rock":
        if comp == "Rock":
            print("It's a draw!\n")
        if comp == "Paper":
            print(oppo,"won!\n")
            comp_score += 1
        if comp == "Scissors":
            print(name," won!\n")
            user_score += 1
        i += 1

    elif user == "Paper":
        if comp == "Rock":
            print(name, "won!\n")
            user_score += 1
        if comp == "Paper":
            print("It's a draw!\n")
        if comp == "Scissors":
            print(oppo,"won!\n")
            comp_score += 1
        i += 1

    elif user == "Scissors":
        if comp == "Rock":
            print(oppo,"won!\n")
            comp_score += 1
        if comp == "Paper":
            print(name, "won!\n")
            user_score += 1
        if comp == "Scissors":
            print("It's a draw!\n")
        i += 1

    else:
        print("Please enter valid input!\n")



winner = max(user_score,comp_score)
diff = abs(user_score - comp_score)

print("Score of",name,": \n",user_score)
time.sleep(1)
print("Score of",oppo,": \n",comp_score)
time.sleep(1)

if winner == user_score:
    print(name,"won by " + str(diff) + " points.\n")
else:
    print(oppo,"won by "  + str(diff) + " points.\n",)



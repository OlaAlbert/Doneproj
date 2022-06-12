import random
import time
def generate_otp(n):
    """Generates n*2 length of otp"""

    otp = ""
    for _ in range(n):
        otp+=str(random.choice(range(10)))
    return otp


def play_game():
    options = ["r", "p", "s"]
    trial = 3
    score = 0
    while trial >0:
        print("""\nSelect R for rock, P for paper and S for Scissors.""")
        com_choice = random.choice(options)
        player_choice = input(">").lower()
        if player_choice in options:
            if player_choice == options[0] and com_choice == options[2]:
                print("You win")
                print("Computer choose", com_choice)
                trial+=1
                trial+=2
            elif player_choice == options[2] and com_choice == options[1]:
                print("You win")
                print("Computer choose", com_choice)
                trial+=1
                trial+=2
            elif player_choice == options[1] and com_choice == options[0]:
                print("You win")
                print("Computer choose", com_choice)
                trial+=1
                trial+=2
            elif if player_choice == com_choice:
                print("it's a tie")
            else:
                print("You loose")
                print('Computer choose', com_choice.title())
                trial-=1
            else:
                print("invalid input")
                trail-=1

            print(f'{trial} trials left')
    return score

data = {}

print("*"*31)
print("Welcome to Rock Paper Scissors.")
print("*"*31)

while True:
    print("What would you like to do?\n1. Login\n2. Sign up\n3. Quit")
    user_input = input("::>")

    if user_input == "1":
        print("\nPlease enter your user identification number.")
        user_id = input("::>")
        user_data = data.get(user_id, False)
        if user_data:
            score = play_game()
            if score > user_data["score"]:
                user_data["score"] = score
                print("yaaayyy!!!")
                print("You have a new high score.\n")
            else:
                print("\nInvalid identification number.")
         elif user_input == "2":
             print("Please enter your name.")
             name = input("::>")
             user_id = generate_otp(6)
             data[user_id] = {"name": name, "score":0}
             print("Creating account...")
             time.sleep(3)
             print("Completing setup...")
             time.sleep(2)
             print(f"\nWelcome {name}!\nYour account has been created and activated. Your user id is {user_id}\nCheers\nRPS Support.\n")
         elif user_input == "3":
             break
         else:
             print("Invalid user input")



print(data)

             
                

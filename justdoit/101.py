import random

while True:
    my_answer = input("Chouse: rock, paper or scissors: ")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        break

    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
        print("plz chouse a correct answer")
        continue 

    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_answer}")

    if my_answer == computer_answer:
        print("wooo salah")
        continue
    elif my_answer == "paper" and computer_answer == "rock":
        print("you win")
        break
    elif my_answer == "rock" and computer_answer == "scissors":
        print("the winner")
        break
    elif my_answer == "scissors" and computer_answer == "paper":
        print("yoo menang")
        break
    else:
        print("kalah lu coba lg!")
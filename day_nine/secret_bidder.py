import os

print("Welcome to the secret bidders program!")

bidders = {}
more_people = True
highest_bid = 0
winner = ""

while more_people:
    name = input("What is your name?: ")
    bidders[name] = int(input("What\' your bid?: $"))
    if bidders[name] > highest_bid:
        highest_bid = bidders[name]
        winner = name

    check = input("Are there any other bidders?: 'yes' or 'no' ").lower()

    if check == "yes":
        os.system('clear')
        pass
    elif check == "no":
        os.system("clear")
        more_people = False
    else:
        print("Get Out!!")
        break

print(f"The winner is {winner} with a bid of {bidders[winner]}")

while True:
    pass
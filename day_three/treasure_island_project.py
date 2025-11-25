#welcome
print("Welcome to the Treasure Island Game!!!\nYour mission is to find the treasure!")

result = input("Is the treasure left or right?\n").lower()
if result == "left":

    result = input("Do you wanna swim or wait for the boat?: \n").lower()
    if result == "wait":
        result = input("Which door you wanna open? Red, Yellow or Blue\n").lower()
        if result == "yellow":
            print("Treasure Found! Congrats")
        else:
            print("Failed!")
            exit()

    else:
        print("Failed!")
        exit()
else:
    print("Failed! Game Over :(")


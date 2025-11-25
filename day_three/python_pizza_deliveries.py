#Intro
print("Welcome to python pizza deliverlies!")


#variables
price_small = 15
price_medium = 20
price_large = 25
pepperoni_small = 2
pepperoni_medium = 3
pepperoni_large = pepperoni_medium
cheese_price = 1
price = 0


#inputs
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


#calculations
if size == "S":
    price = price_small
    
    if pepperoni == "Y":
        price += pepperoni_small

        if extra_cheese == "Y":
            price += cheese_price


elif size == "M":
    price = price_medium

    if pepperoni == "Y":
        price += pepperoni_medium

        if extra_cheese == "Y":
            price += cheese_price


else:
    price = price_large

    if pepperoni == "Y":
        price += pepperoni_large

        if extra_cheese == "Y":
            price += cheese_price


#results
print(f"Your final bill is ${price}")

while True:
    pass

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

tip_percentage = total_bill*(tip/100)
final_bill = total_bill + tip_percentage

number_of_pple = int(input("How many people to split the bill?"))

payment = round((final_bill/number_of_pple), 2)

print(f"Each person should pay: ${payment}")

while True:
    pass


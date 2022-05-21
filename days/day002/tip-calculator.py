import os
os.system("cls" if os.name == "nt" else "clear")

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

party_member_payment = round(bill / people * (tip/100 + 1),2)

print(f"Each person should pay: ${party_member_payment:.2f}")



import os
os.system('cls' if os.name == 'nt' else 'clear')

# print("Do you prefer pounds or kilograms?")
# print("1. pounds")
# print("2. kilograms")
# system = input("> ")

height_inches = input("Enter your height in inches: ")
height_feet_part = int(int(height_inches) / 12)
height_inches_part = int(int(height_inches) % 12)
height_inches_squared = int(height_inches) ** 2


print(f"\nBMI table for {height_feet_part}'{height_inches_part}")
print("\n\tCategory\t| Max Weight (pounds)")
print("----------------------------------------------")
print(f"Underweight (Severe)\t| {int(height_inches_squared*16.0/703)}")
print(f"Underweight (Moderate)\t| {int(height_inches_squared*16.9/703)}")
print(f"Underweight (Mild)\t| {int(height_inches_squared*18.4/703)}")
print(f"Normal\t\t\t| {int(height_inches_squared*24.9/703)}")
print(f"Overweight\t\t| {int(height_inches_squared*29.9/703)}")
print(f"Obese (Class I)\t\t| {int(height_inches_squared*34.9/703)}")
print(f"Obese (Class II)\t| {int(height_inches_squared*39.9/703)}")
infinity_symbol = "\u221e"
print(f"Obese (Class III)\t| {infinity_symbol}")


import os
os.system("cls" if os.name == "nt" else "clear")

year = 400

#revist later after complex conditionals
if year % 4:
  print("1not a leap year")
elif year % 100:
  print("2leap year")
elif year % 400:
  print("3not a leap year")
else:
  print("4leap year")

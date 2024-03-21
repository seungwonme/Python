print("Welcome to the Tip Calculator")

bill = input("\033[0;37mWhat was the total bill?\n\033[0m$")
while (not bill.replace(".", "").isdigit()):
  bill = input("\033[0;37mWhat was the total bill?\n\033[0m$")
bill = float(bill)

percentage = input("\033[0;37mWhat percentage tip would you like to give? 10, 12, or 15?\n\033[0m")
# NOTE: or(||), and(&&), not(!) 
while (not percentage.isdigit() | int(percentage) not in [10, 12, 15]):
  percentage = input("\033[0;37mWhat percentage tip would you like to give? 10, 12, or 15?\n\033[0m")
percentage = int(percentage) / 100

people = input("\033[0;37mHow many people to split the bill?\n\033[0m")
while (not people.isdigit()):
  people = input("\033[0;37mHow many people to split the bill?\n\033[0m")
people = int(people)

print(f"Each person should pay: ${round(bill * percentage * people)}")

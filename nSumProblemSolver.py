print("N SUM PROBLEM SOLVER")

validation1 = False
while not validation1:
    try:
        target_number = int(input("Set a target numbered for the sum: "))
    except:
       print("Invalid answer. Try again.")
    else:
        validation1 = True

validation2 = False
while not validation2:
    try:
        numbers = [int(x) for x in input("Insert the list of numbers you wish to test in any order (whitespace separated): ").split()]
    except:
       print("Invalid answer. Try again.")
    else:
       validation2 = True
numbers.sort()

answers = []

for i in numbers:
  for j in numbers:
    if (i+j == target_number):
      answers.append((i, j))

limit = len(answers)/2

while len(answers) > limit :
  answers.pop()

print("Final answer: None.") if answers == [] else print(f"Final answer: {answers}.")
input("Press any key to exit.")
# Age checking with conditionals
age = int(input("Enter your age: "))
if age >= 18 and age > 0:
    print("You are an adult person")
elif age < 18 and age > 0:
    print("You are not an adult person")
else:
    print("Please enter a valid value")

print("\n--- For Loop Example ---")
# For loop example: Print numbers from 1 to 5
for i in range(1, 6):
    print(f"Number from for loop: {i}")

print("\n--- While Loop Example ---")
# While loop example: Print numbers from 1 to 5
i = 1
while i <= 5:
    print(f"Number from while loop: {i}")
    i += 1

print("\n--- Do-While Loop Example (using while loop) ---")
# Do-While loop example: This is simulated using a while loop since Python doesn't have a do-while loop
i = 1
while True:
    print(f"Number from do-while loop: {i}")
    i += 1
    if i > 5:
        break

print("\n--- Iterating over a List with a For Loop ---")
# Iterating over a list with a for loop
colors = ["red", "green", "blue", "yellow", "purple"]
for color in colors:
    print(f"Color: {color}")

print("\n--- Iterating with a While Loop until a Condition is Met ---")
# Iterating with a while loop until a condition is met
index = 0
while index < len(colors):
    print(f"Color from while loop: {colors[index]}")
    index += 1

  
  

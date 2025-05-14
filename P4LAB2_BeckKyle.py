# Kyle Beck
# P4LAB2
# 30 APR 2025
# Multiplication tble output.

run_again = "yes"

while run_again.lower() == "yes":
    number = int(input("Enter an integer: "))
    if number >= 0:
        print(f"Multiplication table for {number}:")
        for i in range(1, 13):  # for loop from 1 to 12
            print(f"{number} x {i} = {number * i}")
    else:
        print("Cannot accept negative values.")
    run_again = input("Do you wish to run it again? (yes/no): ")

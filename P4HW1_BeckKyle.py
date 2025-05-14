# Kyle Beck
# P4HW1
# 30 APR 2025
# This program collects and displays scores.

num_scores = int(input("How many scores would you like to enter? "))

scores = []

for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break  # Exit inner loop if score is valid
            else:
                print("INVALID Score entered!!!!")
        except ValueError:
            print("Please enter a valid number.")

avg = sum(scores) / len(scores)

print('----------Results----------')
print('Lowest score:', min(scores))
print('Modified List:', scores)
print('Scores Average:', avg)
if avg >= 90:
    print('Grade: A')
elif avg >= 80:
    print('Grade: B')
elif avg >= 70:
    print('Grade: C')
elif avg >= 60:
    print('Grade: D')
else:
    print('Grade: F')

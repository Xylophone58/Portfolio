# Author: Zachary Mitchell
print("Player 1")
shots_made1 = int(input("Shots Made: "))
shots_attempted1 = int(input("Shots Attempted: "))
print("")

print("Player 2")
shots_made2 = int(input("Shots Made: "))
shots_attempted2 = int(input("Shots Attempted: "))
print("")

print("Player 3")
shots_made3 = int(input("Shots Made: "))
shots_attempted3 = int(input("Shots Attempted: "))
print("")

total_shots_made = shots_made1 + shots_made2 + shots_made3
total_shots_attempted = shots_attempted1 + shots_attempted2 + shots_attempted3

percentage = total_shots_made / total_shots_attempted

print("Total: " + str(total_shots_made) + "/" + str(total_shots_attempted))
print(f'Shooting percentage: {percentage:.2f}%')
# ==========================================
# TASK 5: FOR LOOP
# ==========================================

import random


# ------------------------------------------
# 1. Six-Sided Die
# ------------------------------------------

six_count = 0
one_count = 0
two_six_count = 0

previous_roll = 0

print("----- Dice Rolling -----")

for i in range(20):

    roll = random.randint(1, 6)

    print("Roll", i + 1, ":", roll)

    # Count number of 6s
    if roll == 6:
        six_count += 1

    # Count number of 1s
    if roll == 1:
        one_count += 1

    # Count two 6s in a row
    if roll == 6 and previous_roll == 6:
        two_six_count += 1

    # Store current roll as previous roll
    previous_roll = roll


print("\nNumber of times 6 was rolled:", six_count)
print("Number of times 1 was rolled:", one_count)
print("Number of times two 6s were rolled in a row:", two_six_count)


# ------------------------------------------
# 2. Jumping Jacks Workout
# ------------------------------------------

print("\n----- Jumping Jacks Workout -----")

total_jumping_jacks = 0

for i in range(10):

    # Complete one set of 10
    total_jumping_jacks += 10

    print("\nYou completed", total_jumping_jacks, "jumping jacks.")

    # Check if all 100 are completed
    if total_jumping_jacks == 100:
        print("Congratulations! You completed the workout.")
        break

    # Ask whether the person is tired
    tired = input("Are you tired? (yes/no): ")

    if tired.lower() == "yes" or tired.lower() == "y":

        # Ask whether to skip remaining sets
        skip = input("Do you want to skip the remaining sets? (yes/no): ")

        if skip.lower() == "yes" or skip.lower() == "y":
            print(
                "You completed a total of",
                total_jumping_jacks,
                "jumping jacks."
            )
            break

        else:
            remaining = 100 - total_jumping_jacks
            print(remaining, "jumping jacks remaining.")

    elif tired.lower() == "no" or tired.lower() == "n":

        remaining = 100 - total_jumping_jacks
        print(remaining, "jumping jacks remaining.")

    else:
        print("Please enter yes/y or no/n.")

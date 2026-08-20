# Task 3: List

justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

# 1. Calculate the number of members
print("1. Number of members:", len(justice_league))
print("Justice League:", justice_league)


# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("\n2. After adding Batgirl and Nightwing:")
print(justice_league)


# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("\n3. After making Wonder Woman the leader:")
print(justice_league)


# 4. Separate Aquaman and Flash
# Move Green Lantern between Flash and Aquaman

green_lantern = justice_league.pop(justice_league.index("Green Lantern"))

aquaman_index = justice_league.index("Aquaman")

justice_league.insert(aquaman_index, green_lantern)

print("\n4. After separating Aquaman and Flash:")
print(justice_league)


# 5. Replace the existing list with new members
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("\n5. New Justice League:")
print(justice_league)


# 6. Sort the Justice League alphabetically
justice_league.sort()

print("\n6. Alphabetically sorted Justice League:")
print(justice_league)

print("New leader:", justice_league[0])

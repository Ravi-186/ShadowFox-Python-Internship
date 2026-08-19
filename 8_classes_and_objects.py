# ==========================================
# TASK 8: CLASSES AND OBJECTS
# ==========================================


# Create the Avenger class
class Avenger:

    # Constructor
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    # Method to display superhero information
    def get_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)

    # Method to check whether the superhero is a leader
    def is_leader(self):
        if self.name == "Captain America":
            return True
        else:
            return False


# ------------------------------------------
# Create six Avenger objects
# ------------------------------------------

captain_america = Avenger(
    "Captain America",
    100,
    "Male",
    "Super strength",
    "Shield"
)

iron_man = Avenger(
    "Iron Man",
    48,
    "Male",
    "Technology",
    "Armor"
)

black_widow = Avenger(
    "Black Widow",
    39,
    "Female",
    "Superhuman",
    "Batons"
)

hulk = Avenger(
    "Hulk",
    49,
    "Male",
    "Unlimited Strength",
    "No Weapon"
)

thor = Avenger(
    "Thor",
    1500,
    "Male",
    "Super Energy",
    "Mjölnir"
)

hawkeye = Avenger(
    "Hawkeye",
    47,
    "Male",
    "Fighting Skills",
    "Bow and Arrows"
)


# ------------------------------------------
# Store all Avengers in a list
# ------------------------------------------

avengers = [
    captain_america,
    iron_man,
    black_widow,
    hulk,
    thor,
    hawkeye
]


# ------------------------------------------
# Display information about each Avenger
# ------------------------------------------

for avenger in avengers:

    print("\n----------------------------")

    avenger.get_information()

    if avenger.is_leader():
        print("Leader: Yes")
    else:
        print("Leader: No")
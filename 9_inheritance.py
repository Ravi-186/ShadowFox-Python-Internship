# ==========================================
# TASK 9: INHERITANCE
# ==========================================


# Parent / Base Class
class MobilePhone:

    def __init__(
        self,
        screen_type,
        network_type,
        dual_sim,
        front_camera,
        rear_camera,
        ram,
        storage
    ):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    # Make a call
    def make_call(self, number):
        print("Calling", number)

    # Receive a call
    def receive_call(self, number):
        print("Receiving call from", number)

    # Take a picture
    def take_a_picture(self):
        print("Taking a picture")

    # Display mobile phone information
    def display_info(self):
        print("Screen Type:", self.screen_type)
        print("Network Type:", self.network_type)
        print("Dual SIM:", self.dual_sim)
        print("Front Camera:", self.front_camera)
        print("Rear Camera:", self.rear_camera)
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# ==========================================
# Child Class: Apple
# ==========================================

class Apple(MobilePhone):

    def __init__(
        self,
        model,
        screen_type,
        network_type,
        dual_sim,
        front_camera,
        rear_camera,
        ram,
        storage
    ):

        # Calling parent class constructor
        super().__init__(
            screen_type,
            network_type,
            dual_sim,
            front_camera,
            rear_camera,
            ram,
            storage
        )

        self.model = model

    def display_info(self):
        print("\n----- Apple -----")
        print("Model:", self.model)

        # Calling parent method
        super().display_info()


# ==========================================
# Child Class: Samsung
# ==========================================

class Samsung(MobilePhone):

    def __init__(
        self,
        model,
        screen_type,
        network_type,
        dual_sim,
        front_camera,
        rear_camera,
        ram,
        storage
    ):

        # Calling parent class constructor
        super().__init__(
            screen_type,
            network_type,
            dual_sim,
            front_camera,
            rear_camera,
            ram,
            storage
        )

        self.model = model

    def display_info(self):
        print("\n----- Samsung -----")
        print("Model:", self.model)

        # Calling parent method
        super().display_info()


# ==========================================
# Apple Objects
# ==========================================

apple1 = Apple(
    "iPhone 15",
    "Touch Screen",
    "5G",
    False,
    "12MP",
    "48MP",
    "4GB",
    "64GB"
)

apple2 = Apple(
    "iPhone 16",
    "Touch Screen",
    "5G",
    False,
    "12MP",
    "48MP",
    "4GB",
    "64GB"
)


# ==========================================
# Samsung Objects
# ==========================================

samsung1 = Samsung(
    "Galaxy S24",
    "Touch Screen",
    "5G",
    True,
    "12MP",
    "48MP",
    "4GB",
    "64GB"
)

samsung2 = Samsung(
    "Galaxy A15",
    "Touch Screen",
    "4G",
    True,
    "8MP",
    "32MP",
    "4GB",
    "32GB"
)


# ==========================================
# Display Information
# ==========================================

apple1.display_info()
apple2.display_info()

samsung1.display_info()
samsung2.display_info()


# ==========================================
# Test Mobile Functionalities
# ==========================================

print("\n----- Mobile Functionalities -----")

apple1.make_call("9876543210")
apple1.receive_call("9123456780")
apple1.take_a_picture()

samsung1.make_call("9988776655")
samsung1.receive_call("9112233445")
samsung1.take_a_picture()
# ASSIGNMENT_1

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model}")

    def get_specs(self):
        return f"{self.brand} {self.model} - Storage: {self.storage}GB"

# Subclass demonstrating inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, refresh_rate):
        super().__init__(brand, model, storage)
        self.refresh_rate = refresh_rate

    # Overriding method (polymorphism)
    def get_specs(self):
        base_specs = super().get_specs()
        return f"{base_specs}, Refresh Rate: {self.refresh_rate}Hz"

    def launch_game_mode(self):
        print(f"{self.brand} {self.model} is now in Gaming Mode! 🎮")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S22", 128)
phone2 = GamingPhone("ASUS", "ROG Phone 5", 256, 144)

# Use methods
print(phone1.get_specs())
phone1.make_call("0722-123-456")
phone1.install_app("WhatsApp")

print("\n" + phone2.get_specs())
phone2.make_call("0111-999-888")
phone2.launch_game_mode()


#ASSIGNMENT_2
# Base class (optional)
class Vehicle:
    def move(self):
        print("This vehicle is moving...")

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()


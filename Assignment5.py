# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self._battery = battery  # Protected attribute

    def charge(self, amount):
        if amount < 0:
            print("❌ Cannot charge with a negative amount.")
            return
        self._battery = min(100, self._battery + amount)
        print(f"{self.model} charged to {self._battery}%")

    def specs(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self._battery}% battery."

# Subclass 1: GamingPhone (inherits from Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def specs(self):  # Polymorphism in action
        return f"{self.brand} {self.model} (Gaming Edition): {self.storage}GB storage, {self.cooling_system} cooling, Battery: {self._battery}%"

# Subclass 2: CameraPhone (inherits from Smartphone)
class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, megapixels):
        super().__init__(brand, model, storage, battery)
        self.__megapixels = megapixels  # Private attribute (Encapsulation)

    def get_camera_quality(self):
        return f"Camera quality: {self.__megapixels}MP"

    def specs(self):
        return f"{self.brand} {self.model} (Camera Edition): {self.storage}GB storage, {self.__megapixels}MP camera, Battery: {self._battery}%"

# Subclass demonstrating polymorphism
class Speedster(Superhero):
    def __init__(self, name, universe, speed_level):
        super().__init__(name, "Super Speed", universe)
        self.speed_level = speed_level

    def reveal_identity(self):  # Polymorphism
        return f"{self.name} blazes through the {self.universe} universe at level {self.speed_level} speed!"

# Polymorphism Challenge — Vehicles in Motion
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Demonstrating Polymorphism
def demonstrate_vehicle_movement(vehicle):
    vehicle.move()

if __name__ == "__main__":
    # Create a GamingPhone instance
    gaming_phone = GamingPhone("BrandX", "ModelG", 128, 50, "Liquid Cooling")
    print(gaming_phone.specs())
    gaming_phone.charge(30)

    # Create a CameraPhone instance
    camera_phone = CameraPhone("BrandY", "ModelC", 64, 80, 108)
    print(camera_phone.specs())
    print(camera_phone.get_camera_quality())
    camera_phone.charge(-10)  # Invalid charge

    # Superhero example
    flash = Speedster("Flash", "DC", 10)
    print(flash.reveal_identity())
    flash.set_secret_identity("Barry Allen")
    print(f"Secret Identity: {flash.get_secret_identity()}")

    # Vehicle polymorphism example
    print("\nVehicle Movements:")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        demonstrate_vehicle_movement(v)

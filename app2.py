class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving on the road.")


class Plane(Vehicle):
    def move(self):
        print("✈️ Plane is flying in the sky.")


class Boat(Vehicle):
    def move(self):
        print("🚢 Boat is sailing on the water.")


class Bicycle(Vehicle):
    def move(self):
        print("🚴 Bicycle is pedaling down the lane.")

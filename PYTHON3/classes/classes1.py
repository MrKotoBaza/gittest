class Restaurant():
    restaurant_name = ""
    cuisine_type = ""
    is_open = False

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open!")
        self.is_open = True

    def describe_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is a restaurant of {self.cuisine_type} cuisine")
        if self.is_open:
            print("This restaurant is open")

        else:
            print("This restaurant is closed")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors =  flavors

    def get_flavors(self):
        print(f"This stand has {len(self.flavors)} sorts of ice cream:")
        for i in self.flavors:
            print("\t"+i.title())


mallerice = IceCreamStand("MallErICE", "ice_cream", ["strawberry", "chocolate", "banana", "caramel"])

mallerice.describe_restaurant()
mallerice.open_restaurant()
mallerice.get_flavors()






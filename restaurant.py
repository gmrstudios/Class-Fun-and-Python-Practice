class Restaurant():
# A simple attempt to make a restaurant class.

    def __init__(self, restaurant_name, cuisine_type, chef_name):
        """Initialize the attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.chef_name = chef_name
        self.number_served_total = 0
        self.number_served_today = 0

    def describe_restaurant(self):
        description = ("This restaurant is called " +
        self.restaurant_name + " and it serves " + self.cuisine_type  + "." +
        "\nTonight, you will be served by " + self.chef_name + ".")
        return description

    def open_restaurant(self):
        print("The restaurant called " + self.restaurant_name +
        " is open for business, \nserving " + self.cuisine_type)
        print("In its history, " + self.restaurant_name + " has served " +
        str(self.number_served_total) + " customers.")

    def initial_set_number_served(self, customers):
        self.number_served_total = customers

    def increment_number_served(self, today):
        self.number_served_today += today
        self.number_served_total += today

    def reset_daily_total(self):
        self.number_served_today = 0

class Ice_Cream_Stand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, chef_name):
        super().__init__(restaurant_name, cuisine_type, chef_name)
        self.flavors = ["Vanilla"]

    def describe_flavors(self):
        description = ("This restaurant is called " +
        self.restaurant_name + " and it serves the following flavors "
        + str(self.flavors) + ".")
        return description

    def set_new_flavors(self, flavors):
        self.flavors.append(flavors)


#MAIN

my_new_restaurant = Restaurant("Thai Orchid", "Thai cuisine", "Ahmed Rosario")

print(my_new_restaurant.describe_restaurant())
my_new_restaurant.open_restaurant()
my_new_restaurant.initial_set_number_served(10)
my_new_restaurant.increment_number_served(100)
print("Today's number served for " + my_new_restaurant.restaurant_name + " is " +
str(my_new_restaurant.number_served_today) + " customers.")
my_new_restaurant.increment_number_served(100)
print("Total number served for " + my_new_restaurant.restaurant_name + " is " +
str(my_new_restaurant.number_served_total) + " customers.")
my_new_restaurant.reset_daily_total()
print("Today's number served for " + my_new_restaurant.restaurant_name + " is " +
str(my_new_restaurant.number_served_today) + " customers.")
print("Total number served for " + my_new_restaurant.restaurant_name + " is "
+ str(my_new_restaurant.number_served_total) + " customers.")

new_flavors = ["Rocky Road", "Caramel", "Chocolate Chip", "Peanut Butter"]
plainwell_ice_cream = Ice_Cream_Stand("Plainwell Ice Cream", "ice cream", "Laura Gaylord")

print(plainwell_ice_cream.describe_restaurant())
print(plainwell_ice_cream.describe_flavors())
plainwell_ice_cream.open_restaurant()
plainwell_ice_cream.initial_set_number_served(10)
plainwell_ice_cream.increment_number_served(100)
plainwell_ice_cream.set_new_flavors(new_flavors)
print(plainwell_ice_cream.describe_flavors())
print("Today's number served for " + plainwell_ice_cream.restaurant_name + " is " +
str(plainwell_ice_cream.number_served_today) + " customers.")
plainwell_ice_cream.increment_number_served(100)
print("Total number served for " + plainwell_ice_cream.restaurant_name + " is " +
str(plainwell_ice_cream.number_served_total) + " customers.")
plainwell_ice_cream.reset_daily_total()
print("Today's number served for " + plainwell_ice_cream.restaurant_name + " is " +
str(plainwell_ice_cream.number_served_today) + " customers.")
print("Total number served for " + plainwell_ice_cream.restaurant_name + " is "
+ str(plainwell_ice_cream.number_served_total) + " customers.")

my_second_restaurant = Restaurant("Rustica", "European cuisine", "Gustav Maurin")
print(my_second_restaurant.describe_restaurant())

my_other_restaurant = Restaurant("Sushi Chiyo", "Sushi", "Ito Itawa")
print(my_other_restaurant.describe_restaurant())

my_other_restaurant.open_restaurant()

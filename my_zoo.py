"""
Create your own zoo.
This is a simple example of how to use the Zoo class.

"""
from zoo import Zoo
from animal import Animal

# Initialise the zoo
my_zoo = Zoo()

# Create some animals and add to the Zoo
my_zoo.add_animal(Animal(species="lion", name="Fred", legs=4, noise="Roooaaaar"))
my_zoo.add_animal(Animal(species="lion", name="Kate", legs=4, noise="Rooaar"))
my_zoo.add_animal(Animal(species="bear", name="Pete", legs=2, noise="Grrrrr"))
my_zoo.add_animal(Animal(species="bear", name="Suzy", legs=2, noise="Grrrraaar"))
my_zoo.add_animal(Animal(species="snake", name="John", legs=0, noise="Hisssss"))

# See who needs feeding
my_zoo.whos_hungry()

# Feed the Bears
my_zoo.feed_animals(species="bear")

# Check Bears are fed
my_zoo.whos_hungry()

# Feed the Lion
my_zoo.feed_animals(species="lion")

# Check Lions are fed
my_zoo.whos_hungry()

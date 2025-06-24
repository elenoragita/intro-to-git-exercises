"""
Module to define an Animal class.
"""

class Animal():
    """
    Represents an animal
    """
    def __init__(self, species, name, legs, noise, age=0):
        """
        Initialize a new Animal.

        Args:
            species (str): The species of the animal.
            name (str): The name of the animal.
            legs (int): Number of legs the animal has.
            noise (str): The noise the animal makes.
        """
        self.species = species
        self.name = name
        self.legs = legs
        self.noise = noise
        self.age = age
        self.is_hungry = True  # Animals start out hungry

    def make_noise(self):
        """
        Print the noise the animal makes.
        """
        pass

    def feed(self):
        """
        Feed the animal, set its hunger status to False, and make it produce its noise.
        """
        pass

    def add_year(self):
        """
        Increment the age of the animal by one year.
        """
        pass

    def info(self):
        """
        Print information about the animal.
        """
        pass

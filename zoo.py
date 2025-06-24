"""
Module to define a Zoo class.
"""

class Zoo():
    """
    Represents a zoo containing multiple animals.
    """
    def __init__(self):
        """
        Initialize a new Zoo with an empty list of animals.
        """
        self.animals = []

    def add_animal(self, animal):
        """
        Add an animal to the zoo.

        Args:
            animal (Animal): The animal to add.
        """
        pass

    def feed_animals(self, species="all"):
        """
        Feed animals in the zoo, optionally filtering by species.

        Args:
            species (str or list): Species to feed, or "all" for all species.
        """
        pass

    def whos_hungry(self):
        """
        Print the hunger status of all animals in the zoo.
        """
        pass

    def list_animals(self):
        """
        Print info for all animals in the zoo.
        """
        pass

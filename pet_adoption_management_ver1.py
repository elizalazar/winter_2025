"""
Title: Pet Adoption Management
Author: Eliza Lazar
Start Date: December 21, 2025
Version: 1
Description: Application for storing and listing pets. Allows addition of pets, and the marking of adoption.
"""

# Global Constants and Variables
pets = []
next_pet = 1

class Pet:
    """
    
    """
    def __init__(self, pet_id, name, type, age, adopted):
        """
        self: instance of class (itself)
        pet_id: type int - identification number
        name: type string - given name
        type: type string - type of animal (cat, dog, bird, rabbit, etc)
        age: type int - recorded age
        adopted: type boolean - whether pet has been adopted


        """
        self.pet_id = int(pet_id)
        self.name = str(name)
        self.type = str(type)
        self.age = int(age)
        self.adopted = bool(adopted)
    
def show_menu():
    print()

def add_pet():
    print()

def list_pets():
    print()

def adopt_pet():
    print()

def main():
    """

    """
    print("Done!")

if __name__ == "__main__":
    main()
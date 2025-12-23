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
    
    def __str__(self):
        return f"Name: {self.name}\n Type: {self.type}\n Age: {self.age}\n Status: {self.adopted}\n Pet ID: {self.pet_id}0000\n"
    
def show_menu():
    """

    """
    invalid = True;
    print("Welcome to Pet Adoption Centre!\n")
    print("How can we help you today?")
    print("1. View adoptable pets")
    print("2. Add new pet to system")
    print("3. Adopt a pet")
    print("4. Exit application\n")
    choice = int(input("Please submit your choice: "))
    while (invalid):
        if (choice == 1):
            invalid = False
            list_pets()
        elif (choice == 2):
            invalid = False
            add_pet()
        elif (choice == 3):
            invalid = False
            adopt_pet()
        elif (choice == 4):
            invalid = False
            print("Thank you for visiting! Have a nice day :)\n")
            exit()
        else:
            choice = int(input("Sorry, we didn't quite get that. Please submit your choice: "))

def add_pet():
    """

    """
    global next_pet
    print("\nPaperwork for New Arrivals:\n")
    name = input("Pet name: ")
    type = input("Pet Type: ")
    age = input("Pet age: ")
    pet = Pet(next_pet, name, type, age, False)
    pets.append(pet)
    next_pet += 1
    show_menu()

def list_pets():
    """

    """
    print("\nCurrent Adoptables:\n")
    global next_pet
    global pets
    invalid = True
    for pet in pets:
        print(pet)
    print("What would you like to do?")
    print("1. Go back to menu")
    print("2. View specific pet (Under construction)")
    choice = int(input("What would you like to do? "))
    while (invalid):
        if (choice == 1):
            invalid = False
            show_menu()
        elif (choice == 2):
            choice = int(input("Sorry, that feature is currently unavailable. What would you like to do? "))
        else:
            choice = int(input("Sorry, we didn't quite get that. What would you like to do? "))


def adopt_pet():
    """

    """
    print("Adopt\n")

def main():
    """

    """
    show_menu()

if __name__ == "__main__":
    main()
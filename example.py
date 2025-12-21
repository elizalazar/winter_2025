'''
Pokedex Entry
Implemented health identification methods, such as lose of health, status of
life, and reviving of pokemon to the class Pokemon.
By: Eliza Lazar
When: December 1/2024
''' 

class Pokemon:
    '''
    An object in this class represents a single pokemon.
    A pokemon has a name and stats (attack, defense, health) that go
    alongside it.
    '''
    
    def __init__(self, name, attack, defense, max_health, current_health):
        '''
        self - instance of the class (itself)
        name - type string for name of Pokemon
        attack - type int for attack stat of Pokemon
        defense - type int for defense stat of Pokemon
        max_health - type int for maximum health of Pokemon
        current_health - type int for current health of Pokemon
        
        Initializes (creates) a pokemon object with a name, attack
        stat, defense stat, max_health stat, and current_health stat.
        
        Returns: None
        Side Effects: Creates a pokemon object
        
        Examples:
        see pokemon1.py
        '''
        self.name = str(name)
        self.attack = int(attack)
        self.defense = int(defense)
        self.max_health = int(max_health)
        self.current_health = int(current_health)
    
    
    def __str__(self):
        '''
        self - instance of the class (itself)
        
        Returns a string representation of the Pokemon. Contains the name, 
        current health, and maximum health in this format:
           <name> (health: <current_health>/<max_health>)
           
        Returns: str
        
        Examples:
        see pokemon1.py
        '''
        return_string = f"{self.name} (health: {self.current_health}/{self.max_health})"
        return return_string
    
    
    def lose_health(self, amount):
        '''
        self - instance of the class (itself)
        amount - type int for lost health of Pokemon
        
        If amount is less than current_health, decreases the value of the 
        object's current_health attribute by amount.
        If amount is greater than or equal to current_health, set the value of 
        the object's current_health attribute to 0.
        If the amount is negative, do nothing.
        
        Returns: None
        Side Effects: Changes pokemon's current_health to reflect damage.
        
        Examples:
        a1 = Pokemon("Name", 32, 15, 23, 23)
        a1.lose_health(13)
        -> None
        Side Effects: a1's current_health is now 10
        
        a2 = Pokemon("344", 30, 1, 23, 0)
        a2.lose_health(13)
        -> None
        Side Effects: No change to current_health
        
        a3 = Pokemon("344", 30, 1, 23, 20)
        a3.lose_health(13)
        -> None
        Side Effects: a3's current_health is now 7
        
        a4 = Pokemon("344", 30, 1, 23, 2)
        a4.lose_health(13)
        -> None
        Side Effects: a4's current_health is now 0
        
        a5 = Pokemon("Apples", 30, 1, 23, 17)
        a5.lose_health(17)
        -> None
        Side Effects: a5's current_health is now 0
        
        a6 = Pokemon("Apples", 30, 1, 23, 17)
        a6.lose_health(-17)
        -> None
        Side Effects: No change to current_health
        '''    
        if amount < self.current_health and amount >= 0:
            self.current_health = self.current_health - amount
        elif amount >= self.current_health:
            self.current_health = 0
            
            
    def is_alive(self):
        '''
        self - instance of the class (itself)
        
        Returns a boolean indicative of whether the Pokemon is still alive, 
        so if object's current_health is greater than 0, it returns True. False
        is returned if otherwise.
        
        Returns: bool
        
        Examples:
        a1 = Pokemon("Name", 32, 15, 23, 23)
        a1.is_alive()
        -> True
        
        a2 = Pokemon("344", 30, 1, 23, 0)
        a2.is_alive()
        -> False
        
        a3 = Pokemon("344", 30, 1, 23, 20)
        a3.is_alive()
        -> True
        
        a4 = Pokemon("344", 30, 1, 23, 2)
        a4.is_alive()
        -> True
        ''' 
        is_alive = False
        if self.current_health > 0:
            is_alive = True
        return is_alive
                  
                  
    def revive(self):
        '''
        self - instance of the class (itself)
        
        Sets the object's current_health to its max_health to 'revive' the 
        Pokemon. Then prints a message stating the Pokemon has been revived.
        
        Returns: None
        Side Effects: Sets object's current_health to max_health and prints
                      message to screen.
        
        Examples:
        a1 = Pokemon("Name", 32, 15, 23, 23)
        a1.revive()
        -> None
        Side Effects: a1's current_health is now 23 & prints...
        Name has been revived!
        
        a2 = Pokemon("344", 30, 1, 23, 0)
        a2.revive()
        -> None
        Side Effects: a2's current_health is now 23 & prints...
        344 has been revived!
        
        a3 = Pokemon("344", 30, 1, 23, 20)
        a3.revive()
        -> None
        Side Effects: a3's current_health is now 23 & prints...
        344 has been revived!
        
        a4 = Pokemon("344", 30, 1, 23, 2)
        a4.revive()
        -> None
        Side Effects: a4's current_health is now 23 & prints...
        344 has been revived!
        ''' 
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")    
    

def main():
    '''
    Not applicable
    
    Creates two pokemon objects using the Pokemon class:
       pokemon1 - "“Pikachu”, 55, 40, 35, 35
       pokemon2 - “Bulbasaur”, 49, 49, 45, 45
    Uses an f-string to print a welcome message using the identifiers 
    pokemon1 and pokemon2. Then follows the provided testing code to determine
    the functionality of the revive, is_alive, and lose_health methods.
    
    Returns: None
    Side Effects: Prints welcome message for specified pokemon objects, and then
                  evaluates and prints testing code.
    
    Examples:
    main()
    -> None
    Side Effects: Prints...
    Welcome Pikachu (health: 35/35) and Bulbasaur (health: 45/45)!
    ... (then evaluates testing code)
    '''
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45) 
    print(f"Welcome {pokemon1} and {pokemon2}!")
    
    '''
    PROVIDED TESTING CODE - KEEP THIS CODE IN YOUR SUBMISSION
    '''
    print('\n-- TESTS FOR PART 2--')

    # Test is_alive method
    print('Is Pikachu alive?', pokemon1.is_alive())  # Expected: True
    print('Is Bulbasaur alive?', pokemon2.is_alive())  # Expected: True

    # Test lose_health method
    pokemon1.lose_health(10)
    print(f'\nAfter losing 10 health, {pokemon1}')  # Expected: Pikachu (health: 25/35)
    pokemon2.lose_health(45)
    print(f'After losing 45 health, {pokemon2}')  # Expected: Bulbasaur (health: 0/45)

    # Test if the Pokémon is alive after losing health
    print('\nIs Pikachu alive?', pokemon1.is_alive())  # Expected: True
    print('Is Bulbasaur alive?', pokemon2.is_alive())  # Expected: False

    # Test revive method
    print('')
    pokemon2.revive()  # Expected: "Bulbasaur has been revived!"
    print(f'After reviving, {pokemon2}')  # Expected: Bulbasaur (health: 45/45)

    # Test if the Pokémon is alive after being revived
    print('\nIs Bulbasaur alive?', pokemon2.is_alive())  # Expected: True


if __name__ == "__main__":
    main()
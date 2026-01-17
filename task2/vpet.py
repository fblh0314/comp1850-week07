# Name: Louis Morais-Jones
#Student ID: 201988627


# Define a class called VirtualPet with the following attributes:
# (1) name - the name of the pet
# (2) energy - the energy points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is needed, as a minimum, for the __init__ method

# Define a class called VirtualPet with the following attributes:
# (1) name - the name of the pet
# (2) energy - the energy points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is needed, as a minimum, for the __init__ method

class VirtualPet:
    '''A class which defines a virtual pet with the attributes energy hunger and name and can carry out actions play, feed and sleep.'''

    def __init__(self, name, energy = 10, hunger = 0):
        self.energy = energy
        self.hunger = hunger
        self.name = name

    def play(self):
        '''Method to play with the pet, it reduces energy by 2 and increases hunger by 2, the method returns a message if the pet is too tired to play.'''   
        if self.energy < 2:
            return f"{self.name} is too tired to play!"
        else:
            self.energy -= 2
            self.hunger += 2

    def feed(self):
        '''Method to feed the pet (reduces hunger by 3) and if hunger becomes negative it resets to 0 and returns a message stating the pet is overfed.'''    
        self.hunger = self.hunger - 3
        if self.hunger < 0:
            self.hunger = 0
            return f"{self.name} is overfed!"

    def sleep(self):
        '''Method to let the pet sleep, it increaes its' energy by 10.'''        
        self.energy = self.energy + 10

    def __str__(self):
        '''Method which returns pet details including their name, ergy level and hunger level..'''   
        return f"{self.name} has {self.energy} energy points and hunger level {self.hunger}"

    def __eq__(self, other):
        '''Method which returns true if all attributes are equal between two pets and false otherwise.'''  
        return (self.name == other.name and 
                self.energy == other.energy and 
                self.hunger == other.hunger)

# This class has the following methods:
# (1) play() - If energy<2, report in the format "{name} is too tired to play!".
#     Otherwise simulate playing by reducing the energy by 2 and increase the hunger by 2.
# (2) feed() - Simulate feeding the pet and reducing hunger by 3.
#     If hunger is less than 0, report in the format "{name} is overfed!" and reset hunger to 0.
# (3) sleep() - let the pet sleep and increase the energy by 10.
# (4) __str__() - returns the details of the pet in the format "{name} has {energy} energy points and hunger level {hunger}", 
#     e.g., "Timmy has 100 energy points and hunger level 0"
# (5) __eq__() - returns True if all attributes are identical, False otherwise

# You should test each method in your code before submission.
# Check that attributes are modified as expected
# For example:

''' Tests
Pet = VirtualPet("Timmy",4,3)
print(Pet)
Pet.play()
print(Pet)
Pet.feed()
print(Pet)
Pet.sleep()
print(Pet)
'''
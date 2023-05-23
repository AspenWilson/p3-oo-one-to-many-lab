class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all= []

    def __init__(self, name, pet_type, owner= None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Invalid pet type: {}".format(pet_type))
        self._owner = owner
        if self not in Pet.all:
            Pet.all.append(self)
    
    @property
    def owner (self):
        return self._owner

class Owner:
    def __init__(self, name):
        self.name = name


    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if pet.pet_type in Pet.PET_TYPES:
            pet._owner = self
        else:
            raise Exception("Invalid pet type")


    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)   
class Items:
    def __init__(self):
        self.name
        self.type
        self.currency_value:  # described in pieces of gold
        self.weight
        self.location




class Weapons(Items):  #instances: cannon, laser
    def __init__(self):
        self.ap

class Armor(Items): # def titanium shield, forcefield, tin shield
    def __init__(self):
        self.def_val

class Engine(Item):
    def __init__(self):
        self.speed

# class Gold(Items):
#     pass

class Heal(Items):
    def __init__(self):
        self.hp_heal

class Key(item):  # symbols as password for final room
    pass




class Inventory:
    def __init__(self):
        self.inventory = []
        self.max_weight

    def container(self):
        pass

    def crud(self): #create, replace, update, delete
        pass

    def display(self):
        pass

    def display_gold_value(self):
        pass





class Balloon:
    # Health as Integer
    # Colour as String
    # Defence_item as String
    def __init__(self, defence_item, colour):
        # private attributes
        self.defence_item = defence_item
        self.colour = colour
        self.health = 100

    def GetDefenceItem(self):
        return self.defence_item

    def GetHealth(self):
        return self.health

    def ChangeHealth(self, healthAdd):
        self.health += healthAdd

    def CheckHealth(self):
        print(self.health)
        if self.health <= 0:
            return True
        else:
            return False

    def Defend(self, MyBalloon):
        pass


defenceItem = input("Enter a new defence item: ")
colour = input("Enter a new colour: ")
Balloon1 = Balloon(defenceItem, colour)




Balloon1.ChangeHealth(20)
print(Balloon1.CheckHealth())


from Creature import Creature
from Equipment import Equipment
import theGame

class Hero(Creature):
    """The hero of the game.
        Is a creature. Has an inventory of elements. """

    def __init__(self, name="Hero", hp=10, abbrv="@", strength=2,toxicity=0,poisoned=0):
        Creature.__init__(self, name, hp, abbrv, strength,toxicity,poisoned)
        self.gold=0 #or n'est plus dans l'iventaire
        self._inventory = []

    def description(self):
        """Description of the hero"""
        return Creature.description(self) +"(Gold:" + str(self.gold) + ")"+ str(self._inventory)

    def fullDescription(self):
        """Complete description of the hero"""
        res = ''
        for e in self.__dict__:
            if e[0] != '_':
                res += '> ' + e + ' : ' + str(self.__dict__[e]) + '\n'
        res += '> INVENTORY : ' + str([x.name for x in self._inventory])
        return res

    def checkEquipment(self, o):
        """Check if o is an Equipment."""
        if not isinstance(o, Equipment):
            raise TypeError('Not a Equipment')

    def take(self, elem):
        """The hero takes adds the equipment to its inventory"""
        self.checkEquipment(elem)
        if elem.name == "gold":
            self.gold = self.gold + 1
            return True
        elif len(self._inventory) < 10:
            self._inventory.append(elem)  ### G.IV : take renvoie désormais un booléen selon que l'item est effectivement pris ou non, le gold est stocké hors de l'inventaire, et la taille de l'inventaire ne doit pas dépasser 10
            return True
        else:
            theGame.theGame().addMessage(" to take this equipment,use or destroy something")
            return False

    def destroy(self,elem):      #G.IV : Méthode permettant de détruire un élément de l'inventaire
        self._inventory.remove(elem)
        theGame.theGame().addMessage("You destroyed the" + elem.name)
    

    def use(self, elem):
        """Use a piece of equipment"""
        if elem is None:
            return
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        if elem.use(self):
            self._inventory.remove(elem)

from Element import Element
import theGame

class Creature(Element):
    """A creature that occupies the dungeon.
        Is an Element. Has hit points and strength."""

    def __init__(self, name, hp, abbrv="", strength=1,toxicity=0,poisoned=0):
        Element.__init__(self, name, abbrv)
        self.hp = hp
        self.strength = strength
        self.toxicity=toxicity #nombre de mouvement ou le poison va agir
        self.poisoned=0  #nombre de mouvement ou on est empoisoné,
        self.protection=0
        
    def description(self):
        """Description of the creature"""
        if self.poisoned>0:
            b="(PoisonedIsEffective:"+str(self.poisoned)+")"
        else:
            b=""
        return Element.description(self) + "(" + str(self.hp) + ")" + "(P:" + str(self.protection) + ")"+b


    def poison(self):
        "effect of the poison"
        if self.poisoned>0:
            if self.protection>0:
                self.protection-=1
                self.poisoned-=1
                theGame.theGame().addMessage("The poison makes you lose 1 protection")
            else:
                self.hp-=1
                self.poisoned-=1
                theGame.theGame().addMessage("The poison makes you lose 1 hp")
        
            
    def meet(self, other):
        """The creature is encountered by an other creature.
        The other one hits the creature. Return True if the creature is dead."""
        if other.toxicity>0:
            self.poisoned+=other.toxicity
            
        if other.poisoned>0:
            other.poison()
        x=1
        while x<=other.strength :    #le x permet de retirer le bon nombre de hp dans le cas ou 0<self.protection<other.strength
            if self.protection>0 :
                self.protection -= other.strength
                x+=1
            else:
                self.hp -= other.strength
                x+=1
        theGame.theGame().addMessage("The " + other.name + " hits the " + self.description())
        if self.hp > 0:
            return False
        return True

   

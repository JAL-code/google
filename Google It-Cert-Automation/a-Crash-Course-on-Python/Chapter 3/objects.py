class Apple:
    pass # empty class

class ApplePie:
    color = ""
    flavor = ""

jonagold =  Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.color, jonagold.flavor)

print(jonagold.color.upper())

golden = Apple()
golden.color = "yellow"
golden.flavor = "sweet"

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
     x=0
     x=you.apples
     you.apples=me.apples
     me.apples=x
     return you.apples, me.apples

def exchange_ideas(you, me):
     x=0
     x=you.ideas
     you.ideas += me.ideas
     me.ideas += x
     return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

class Piglet:
    def speak(self):
        print("oink oink")

hamlet = Piglet()
hamlet.speak

class Piglet2:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink! Oink!".format(self.name))

hamlet2 = Piglet2()
hamlet2.name = "Carl"
hamlet2.speak

petunia = Piglet2()
petunia.name = "Petunia"
petunia.speak

class Apple3:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
jonagold = Apple3("red", "sweet")
print(jonagold.color)

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is " + self.name

# Create a new instance with a name of your choice
some_person = Person("Jack")
# Call the greeting method
print(some_person.greeting())

class Onion:
    """define function"""
    def __init__(self, color, flavor):
        """define color and flavor"""
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This onion is {} and its flavor is {}".format(self.color, self.flavor)

Vidalia = Onion("white", "sweet")
print(Vidalia)
help(Onion)
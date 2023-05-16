#Duck typing = concept where the class of an object is less important than the methods
#              class  type is not cheecked if minimum methods /attributes are present
#              if its walk like a duck and it talk like a duck then its a duck  

class Duck:

    def Walk(self):
        print("Duck is Walking")
    
    def Talk(self):
        print("Duck is Quacking")

class Chicken:

    def Walk(self):
        print("Chicken is Walking")
    
    def Talk(self):
        print("Chicken is coocoo")

class Person:

    def Catch(self,duck):
        duck.Walk()
        duck.Talk()
        print("You caught the critter!")

duck=Duck()
chicken=Chicken()
person=Person()

person.Catch(chicken)
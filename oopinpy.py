#object oriented programming in python
class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
        
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shoot films")
            
    def speak(self):
        print(self.name,"says how are u")
        
tom=Human("tom_cruise","actor")
tom.do_work()
tom.speak()
maria=Human("maria","tennis player")
maria.do_work()
maria.speak()
###########################################
class vehicle:
    def general_usage(self):
        print('general use:transportation')
class car(vehicle):
    def __init__(self):
        print("i am car")
        self.wheels=4
        self.has_roof=True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use:commute to work,vacation with friends")
        
class motorcycle(vehicle):
    def __init__(self):
        print("I am motor cycle")
        self.wheels=2
        self.has_roof=False
        
    def specific_usage(self):
        self.general_usage()
        print("specific use:local commutation,racing")
        
c=car()
m=motorcycle()
c.specific_usage()
m.specific_usage()
#########################################
#multiple inheritance
class father():
    def skills(self):
        print("i like gardening")
        
class mother():
    def skills(self):
        print("i like cooking")
        
class child(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("i like sports")
        
c=child()
c.skills()

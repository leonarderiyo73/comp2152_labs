class Person:
    def __init__(self, p_name, p_age, p_height):
        self.name = p_name
        self.age = p_age
        self.height = p_height
        self.public_prop = "I'm public"

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object.")

person1 = Person("Mark", 20, 6)

print("The name of person1 is:"+ str(person1.name))
#print("Private: "+str(person1._name)) # This will cause an error
person1.name = "Alfred"
print("The name of person1 is:"+ str(person1.name))

print("Public: " + str(person1.public_prop))

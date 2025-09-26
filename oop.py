class cSStudent :
    # CLass Variable
    stream = 'cse'
    # The init method orconstructor
    def __init__(self, s_name, roll):
        #Instance variable/attribute
        self.s_name = s_name
        self.roll = roll
    
    #Instance method
    def setAddress(self, Address):
        self.Address = Address
    
    #Retrieve Instance variable
    def getAddress(self):
        return self.Address

#Driver code/ object creation/ instance creation
student1 = cSStudent("Shaiyan", 1)
student1.setAddress("Jhenaidah, Bangladesh")
print(f"I'm {student1.s_name}, my roll is {student1.roll} and I live in {student1.getAddress()}")

student2 = cSStudent("Tahsin", 2)
student2.setAddress("Dhaka, Bangladesh")
print(f"I'm {student2.s_name}, my roll is {student2.roll} and I live in {student2.getAddress()}")

#Object of CSStudent class
a = cSStudent("Alex", 3)
b = cSStudent("Steven", 4)

print(a.stream)#Print cse
print(b.stream)#Print cse
print(a.roll)#Print 3

#Class variables can be accessed using class name also
print(cSStudent.stream)#Print cse
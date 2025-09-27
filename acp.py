class Bird:
    def __init__(self, name, color, origin):
        self.name = name
        self.color = color
        self.origin = origin

    def displsy(self):
        return f"{self.name} is from {self.origin} and they are {self.color} in color generally"
    
Bird1 = Bird("Doel", "Black and White", "Bangladesh")
Bird2 = Bird("PArrot", "Red and Green", "Bangladesh")
Bird3 = Bird("Macou", "Blue-Yellow-Red", "Amazon forest")


print(Bird1.displsy())
print(Bird2.displsy())
print(Bird3.displsy())
    
        
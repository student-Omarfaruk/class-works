class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        pi=22/7

        return pi*self.radius*self.radius
r=float(input("Enter the number:"))
c=Circle(r)
print("The area of circle is:",c.area())

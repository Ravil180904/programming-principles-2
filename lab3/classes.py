#3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Rectangle():
    def rec(self, l, w):
        self.length = l
        self.width = w
    def area(self):
        return self.length * self.width
result = Rectangle(5, 10)
print(result.area())
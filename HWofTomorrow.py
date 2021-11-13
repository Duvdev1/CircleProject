
import math
class circle():
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
       return self.radius
    def calc_area(self):
        return math.pi * self.radius ** 2
    def calc_hekef(self):
        return 2 * math.pi * self.radius

new_circle = circle(5)
print('radius: ', new_circle.radius)
print('hekef: ', new_circle.calc_hekef())
print('area: ',new_circle.calc_area())

#in the question given by itai, we were requested to print the radius, hekef and area under
# __str__, i couldnt do the printing from __str__, it didnt work for me, i hope you can let me know what was the problem.
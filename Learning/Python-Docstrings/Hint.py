from typing import List
import typing
def reverse(name:typing.Union[str,list]) -> typing.Union[str,list]:
    return name[::-1]

#print(reverse('Rajalakshmi'))
#print(reverse(['Rajalakshmi','Kamalanathan']))

def add_num (a: typing.List[float])-> float:
    return sum (a)

print(add_num([1 ,2.89 ,3.0]))

class typehint:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return f'{self.x}'
    def __add__(self, other):
        return self.x + other.x
num1 = typehint(20)

num2 = typehint(40)
#print(num1,num2)
#print(num1 + num2)

def add(x: typehint, y: typehint) -> int:
    return x + y

print(add(num1, num2))
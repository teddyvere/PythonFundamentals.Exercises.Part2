#returns exponet of a and b
def exponentiate(a, b):
    return a ** b

""""squares a to the 4th power"""
def raise_to_fourth_power(a): 
    return a ** 4

square = lambda x: exponentiate(x,2)

cube = lambda x: exponentiate(x,3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
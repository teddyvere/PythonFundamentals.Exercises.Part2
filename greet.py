def greet(name):
    print('Hello ' + name )

def nameInput():
    nameString = input('Provide a name ')
    return nameString
    print(nameString)

greet(nameInput())
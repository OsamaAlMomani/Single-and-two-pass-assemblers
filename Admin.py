import importlib
import Admin
def a ():
    animal='DD'
    def b():
        nonlocal animal
        animal = 'BB'
        print (animal)
    
    print (animal)
    b()
    print(animal)
animal ='CC'    
a()    
print (animal)

input ('enter')

importlib.reload(Admin)
 

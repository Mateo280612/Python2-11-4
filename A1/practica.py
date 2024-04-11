datos = [ i for i in range(10,21)]
print(datos)

names = ['Ana','Pedro','Juan']
names_2= [ i.upper() for i in names]
print(names_2)
list_pares=[]
numbers_3 = [1,2,3,4,5,6]
for i in numbers_3:
    if i>3:
        list_pares.append(i)
print(list_pares)
list_pares_2=[i for i in numbers_3 if i>3 ]
print(list_pares)

def greet ():
    return True

print(greet())

def suma(a,b):
    print(a,b)
    return a+b

print(suma(b=2,a=3))

def descuento(precio,descuento=0):
    return precio-descuento

print(descuento(100))

def practica(num):
    if num % 2 == 0 :
        return 'Es par'
    else:
        return 'Es impar'

print(practica(28))

def pares (*args):
    for i in args:
        print (i)

print(pares(4,'Pedro',5.5,True))

def pares (lista):
    list = []
    for i in lista:
        if i % 2 ==0:
            list.append(i)
    return list
        
array = [2,3,4,6,3,10,12]
print(pares(array))

def ParesMayores (lista):
    new_list = []
    for i in lista:
        if i > 6:
            new_list.append(i)
    
    return new_list

print(ParesMayores(pares(array)))

list()
        
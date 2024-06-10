# Exercise 1
for i in range(10):
    print(i)

# Exercise 2
def suma(num1, num2, num3):
    return num1 + num2 + num3

#print(suma(1, 2, 3))

# Exercise 3
suma_lambda = lambda num1, num2, num3: num1 + num2 + num3

#print(suma_lambda(1, 2, 3))

# Exercise 4
nombre = 'Enrique'
#lista_nombre = 'Jessica', 'Paul', 'Enrique', 'George', 'Henry', 'Adán'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

def existe_nombre():
    existe = False

    for n in lista_nombre:
        if n == nombre:
            existe = True
            break
    
    if existe:
        print(f"El nombre {nombre} SÍ está en la lista.")
    else:
        print(f"El nombre {nombre} NO está en la lista.")

existe_nombre()
#sumar
# n1, solicita un numero
# n2, solicita otro numero
# return, la suma de los dos números

def sumar(n1,n2):
    return n1+n2 


# Restar
# n1, solicita un numero
# n2, solicita otro numero
# return, la resta de los dos números
def restar(n1,n2):
      return n1-n2

# Multiplicar
# n1, solicita un numero
# n2, solicita otro numero
# return, la multiplicacion de los dos números
def multiplicar (n1,n2):
    return n1*n2

# Dividir
# n1, solicita un numero
# n2, solicita otro numero
# return, la División de los dos números
def dividir (n1,n2):
    return n1/n2

numero1 = 10
numero2 = 5

def operaciones(nombre,n1,n2):
     print(nombre)
     print(15*"-")
     print("suma:",sumar(n1,n2))
     print("Resta:",restar(n1,n2))
     print("multiplicar:",multiplicar(n1,n2))
     print("Dividir:",dividir(n1,n2))
     print(15*"-")

operaciones("Beyla",10,5)
operaciones("Angel",10,15)


def datos(nombre,edad):
     print("Nombre",nombre)
     print("Edad",edad)


datos("Madeley",17)
  
     
     


     

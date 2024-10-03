#ejemplo para calcular el area del triangulo

#vaiables de entrada

base = int(input("ingrese la base: "))
altura = int(input("ingrese la altura: "))

#proceso
def calcularAreaTriangulo(b,a):
    area = (b*a/2)
    return area
#invocar la funcion
resultado = calcularAreaTriangulo(base,altura)
#salida
print(f"el area del triangulo cuya base es {base } y altura {altura} es: {resultado}")

#funciones con argumentos predeterminados
def my_function(country = "colombia"):
    print ("i am from "+country)

#invocar la funcion
my_function()
my_function("sweden")


#argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("el estudiante: "+args[2])

#invocar la funcion
mostrarEstudiantes("Emil", "tobias", "linis", "bill", "andres")


def mostrarCarros(carro1, carro2, carro3):
    print("el carro es: "+ carro2)

mostrarCarros(carro1 = "BMW", carro3 = "ferrari", carro2 = "Ford")




def mostrarCliente(**kwargs):
    print("su apellido es: "+ kwargs["telefono"])

mostrarCliente(nombre = "Tobias", apellido = "Refsnes", direccion = "1212" , telefono = "2323")


def miFuncion():
    pass
x = min(5,10.25)
y = max (5,10,25)
print(x)
print(y)


num1 = pow(7,4)
print(num1)

#modulo de matematicas
import math
num2 =math.sqrt(34)
print(num2)

import math
num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3) #returns 8
print(num4) #returns 7

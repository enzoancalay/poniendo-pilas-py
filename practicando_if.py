numero = 3 

numero = numero + numero 
print(numero)


"filas de numeros con for"

numeros=[2, 3, 4, 5]
for numero in numeros :
    print ( numero * 2)

"armar un programa que imprima la suma de todos los numeros de una lista"


a=0
numeros = [1, 2, 3, 4, 5]

for n in numeros:
    a= n + a
 
print (a)


"contar cuantos numeros impaeres tiene la lista"
cat_impares=0
numeros = range(1,11)
for n in numeros:
    es_impar= n % 2 != 0
    if es_impar :
        cat_impares = cat_impares + 1
    
print (cat_impares)
    





"""🔹 Nivel 1 (fácil)

Número positivo o negativo
Escribí un programa que pida un número y diga si es positivo, negativo o cero.

Edad mínima para votar
Pedí la edad del usuario y decí si puede votar (18 años o más) o no."""


numero= int(input("por favor ingresar un numero : "))
if numero > 0:
    print("Es positivo")
elif numero ==0:
    print ("Es Cero")
else:
    print("Es negativo")


votar= int(input("ingrese su edad por favor: "))

if votar >= 18:
    print("Puede usted votar ")

elif votar <= 0 :
    print("ingrese una edad valida")

else:
    print("No puede votar ")


    

"""🔹 Nivel 2 (intermedio)

Número par o impar
Ingresar un número y mostrar si es par o impar."""

num=int(input("ingrese un numero por favor "))
if num %2 != 0:
    print("Es impar ")
else:
    print("Es par ")





"""Mayor de dos números
Pedí dos números y mostr á cuál es el mayor (o si son iguales)."""

num1= int(input("Ingresar el primer numero: "))
num2= int(input("ingresar el segun numero: "))

if num1==num2:
    input("son iguales") 
elif num1>num2:
    print("Es mayor el primer numero")
else:
    print("Es mayor el segun numero")
    


"""Contraseña correcta
Pedí al usuario que ingrese una contraseña.
Si coincide con "python123", mostrar "Acceso concedido", si no, "Acceso denegado"."""
contra= input("ingresar una contraseña: ")
if contra == "python123":
    print("acceso consedido")

else:
    print("Acceso denegado: ")

    



    

 









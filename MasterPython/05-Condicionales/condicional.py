"""
Una condicional es una estructura de control que permite controlar el flujo del programa. Ejemplo: Si un programa cumple
con una condicion acto seguido se ejecutaran un grupo de instrucciones

#Condicional IF
SI se_cumple_esta_condicion:
    Ejecuta instruccion 1
SINO:
    Ejecuta instruccion 2

#Operadores de comparacion
Codigo     Significado
==         igual que
!=         distinto
<          menor que
>          mayor que
<=         menor o igual que
>=         mayor o igual que
#Operadores Logicos
Codigo     Significado
and        y
or         o
!          negacion
not        no
"""
"""
#Ejemplo 1
print("###########Ejemplo1###########")
#Variables
color = input("Adivina cual es mi color favorito: ")
#Condicion
if color == "rojo":
    print("Nice")
    print("mi color favorito es rojo")
else:
    print("BRUH!!!")
    print("El color es incorrecto")

#Ejemplo 2
print("###########Ejemplo2###########")
#Variables
year = int(input("What year are you?: "))
#Condicion
if year >= 2022:
    print("We are in the year 2022 and beyond")
else:
    print("You are in a year before 2022")
    print(f"you are in the year {year}")

#Ejemplo 3 IF's anidados
print("###########Ejemplo3###########")
#Variables
nombre=input("Cual es tu nombre: ")
provincia=input("Cual es tu ciudad: ")
pais=input("De que pais eres: ")
edad=int(input("Cual es tu edad?: "))
mayoria_edad=18
#Condicion
if edad>=mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if pais != "Panama":
        print(f"{nombre} no es de Panama")
        print(f"{nombre} es de {pais} de la provincia {provincia}")
    else:
        print(f"{nombre} es de Panama y es de la provincia {provincia}")
else:
    print(f"{nombre} no eres mayor de edad")

#Ejemplo 4 Elif
print("###########Ejemplo4###########")
#Variables
dia = int(input("Ingresa un numero para saber que dia sera: "))
#Condicion
if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sabado")
elif dia == 7:
    print("Es Domingo")
elif dia > 7:
    print("Una semana solo tiene 7 dias tontito o bueno para ser mas inclusivo, tontite ;)")

#Ejemplo 5
print("###########Ejemplo5###########")
#Variables
nombre=input("Cual es tu nombre?: ")
edad=int(input("Ingresa tu edad: "))
if edad>=18 and edad<= 65:
    print(f"{nombre} Tiene {edad} la cual es la edad necesaria para trabajar")
else:
    print(f"{nombre} Tiene {edad} esta edad no es la indicada para trabajar")

#Ejemplo 6
print("###########Ejemplo6###########")
#Variables
pais = input("De que pais eres?: ")
if pais == "Panama" or pais == "Colombia" or pais == "Costa Rica":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

#Ejemplo 7
print("###########Ejemplo7###########")
#Variables
pais = input("De que pais eres?: ")
if not (pais == "Panama" or pais == "Colombia" or pais == "Costa Rica"):
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")
"""
#Ejemplo 8
print("###########Ejemplo8###########")
#Variables
pais = input("De que pais eres?: ")
if pais != "Panama" and pais != "Colombia" and pais != "Costa Rica":
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")


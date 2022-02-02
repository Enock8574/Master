#Entrada
nombre = input("Cual es tu nombre?: ")
edad = input("Cual es tu edad?: ")
#Salida
#Se uso el int para convertir la edad a entero, ya que lo que esta dento del print se considera string
print(f"Me alegro de conocerte {nombre} bienvenido, veo que tiene {int(edad)+2}")
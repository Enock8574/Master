"""
Una variable es un contenedor de informacion que dentro guardara un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto
"""
#Desarrollo de variables
escritura = "Master en Python"
escritura2 = "Con Victor Robles"
numero = 45
decimal = 6.7
#Imprimir por pantalla
print(escritura)
print(escritura2)
print(numero)
print(decimal)
print("--------------------------------------------------------")
#Es posible reemplazar los valores de las variables
numero = 77
decimal = 66.6
print(numero)
print(decimal)
print("--------------------------------------------------------")

#Concatenacion
"""
La concatenacion es utilizada para poder unir 2 o mas variables en una linea de codigo
"""
nombre="Enoc"
apellido="Carrera"
web="enoccarreraweb.com.pa"

#Impresion
print(nombre +" "+ apellido +" "+ web)
#Otra Forma de concatenar
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellido,web))
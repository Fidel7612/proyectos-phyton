#Nombre: Fidel Lopez Sandoval
#Matricula: 010400197
#Lic. En Ingenieria En Sistemas Computacionales
letra = 'letras'
#pedimos al usuario que ingrese la palabra
palabra = str(input("Dame la palabra de favor: "))
#se realiza el condicional if para saber si la condicion es verdadera
#se utiliza la funcion len para saber el tamaño de la palabra
if len(palabra) <= 3:
#si se cumple la condicion se muestra el siguiente mensaje
    print("Te faltan letras solo introduciste:",len(palabra))
#se utilza el condicional elif para saber si el tamaño de la palabra cumple con la condicion
elif len(palabra) == 4:
#si se cumple la condicion manda un mensaje siguiente
    print("Introduciste 4 letras palabra correcta",len(palabra))
#igual se utiliza el condicional elif para saber el tamaño de la palabra
#en este caso se utiliza el operador and para establecer 2 condicones
elif len(palabra) >= 5 and len(palabra) <=7:
#al cumplirse una de las 2 condiciones manda el siguiente mensaje
    print("Te faltan letras solo tecleaste la cantidad de letras siguiente:",len(palabra))
#siguiente movimiento otro condicional pero ahora nos pide que la palabra
#coincida con el numero de letras
elif len(palabra) == 8:
#Al cumplirse la condicion manda el siguiente mensaje
    print("Introduciste la palabra correcta contiene letras correctas que son: ",len(palabra))
#se utiliza el condicional elif comparando si la palabra ingresada
#contiene mas de 8 letras
elif len(palabra) > 8:
#si se cumple la condicion manda el siguiente mensaje
    print("Introduciste mas de 8 letras en total son:",len(palabra))
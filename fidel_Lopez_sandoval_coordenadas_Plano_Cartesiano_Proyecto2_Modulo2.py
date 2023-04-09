#Declaramos Nuestras Dos Variables
numero_1 = 0
numero_2 = 0
#Pedimos al usuario que introduzca la coordenas
numero_1= int(input(f"Dame la primer coordenada X: "))
#se realiza el condicional por si ingresa el numero 0
if numero_1 == 0:
#Si se cumple la condicion manda el siguiente mensaje
    print("No se permite el 0 como coordenada")
numero_2= int(input(f"Dame la segunda Coordenada Y: "))
#se realiza el condiconal por si ingresa el numero  0 el usuario
if numero_2 == 0:
#si se cumple la condicon manda el siguiente mensaje
    print("No se permite el numero 0 como coordenada")
#Imprimimos las coordenadas en pantalla
print("Las coordenadas Son: ",numero_1,numero_2)
#realizamos el condicional para saber si las coordenas ingresadas por el usuario son del primer cuadrante
#utilizamos el operador and para hacer la comparacion entre los dos numeros que sean diferente de 0
if numero_1 > 0 and numero_2 > 0:
#si se cumple la condicion nos despliega el mensaje que las coordenas correponden al primer cuadrante
    print("LAS COORDENADAS SE UBICAN EN EL PRIMER CUADRANTE DEL PALNO CARTESIANO")
#Nos imprime las coordenadas
    print(numero_1,numero_2)
elif numero_1 < 0 and numero_2 > 0:
    print("LAS COORDENADAS DE ESTE PUNTO SE UBICAN EN EL SEGUNDO CUADRANTE DEL PLANO CARTESIANO")
    print(numero_1,numero_2)
elif numero_1 < 0 and numero_2 < 0:
    print("LAS COORDENADAS DE ESTE PUNTO SE UBICAN EN EL TERCER CUADRANTE DEL PLANO CARTESIANO")
    print(numero_1,numero_2)
elif numero_1 > 0 and numero_2 < 0:
    print("LAS COORDENADAS DE ESTE PUNTO SE UBICAN EN EL CUARTO CUADRANTE DEL PLANO CARTESIANO")
    print(numero_1,numero_2)
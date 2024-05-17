#Declaramos una variable en 0 para llevar e incrementar nuestro contador
a = 0
#Se pide un While TRUE PARA verificar que el dato introducido por el usuario sea Correcto y numerico
while True:
#Se declara la sentencia try para verificar que el dato introducido por el usuario sea el numerico y verdadera de lo contrario nos va mandar un error
                        try:
#dentro de la sentencia try se declara una variable que guardara la contraseña introducida por el usuario        
                            Password = int(input("Introduce La Contraseña:"))                
                            break
    #En la sentencia except agregamos nuestro contador que se incrementara en 1, de acuerdo a la cantidad de errores
    #que introducimos, si el contador se incrementa a 3 se cumple la condicion IF, y nos despliega el mensaje de los 3 errores fin del programa
                        except ValueError:           
                                a+=1
                                print("La contraseña No Acepta Caracteres solo numeros")
                                if a==3:
                                    print("Introduciste 3 ERRORES fin del Programa")
                                    exit()    
#para la confirmacion de la contraseña de igual manera declaramos una variable en 0, que va ser nuestro contador de errores
b = 0                
#Declaramos un whle true de igual forma para confirmar que la verificacion del la contraseña sea verdadera
while True:        
#se declara la sentencia try donde se pide la confirmacion de la contraseña y se guarda en otra variable 
            try:    
                Contraseña = int(input("Favor de Confirmar la Contraseña:"))
#Se compara la contraseña para verificar si es correcta mediante la condicion if si es correcta nos despiega el mensaje "contraseña correcta"
# de lo contrario nos va mandar un error                
                if Password == Contraseña:
                        print("Contraseña Correcta")
                        break
#en la sentencia except se coloca nuestra variable como contador y si el contador se incrementa a 3 errores nos manda un mensaje 
#de has introducido 3 errores fin del programa
            except ValueError:
                    print("Confirmacion de Contraseña Incorrecta Vuelve a Introducir la contraseña ")
                    b+=1            
                    if b == 3:
                        print("Introduciste 3 ERRORES fin del programa ")
                        exit()
                        break
            

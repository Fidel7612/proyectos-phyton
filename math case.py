
print("M            E               N               U\n")
print("1.- Calculo de La Circunferencia de un Circulo\n")
print("2.- Calculo del Area de un Rectangulo\n")
print("3.- Calculo del Area de un Triangulo Equilatero\n")
print("4.- Calculo del Area de un Cuadrado\n")
print("5.- Salir\n")
while True:
            variables = int(input("Elige Una Opcion:\n"))     
            match variables:
                case 1 :
                    print("C A L C U L O   D  E  L    A  R  E  A    D  E    U  N    C  I  R  C  U  L  O \n")
                    print("Formula: Area = Pi * radio*radio \n")
                    pi = 3.1416
                    print("pi = 3.1416 constante:")
                    r=float(input(f"Dame el Radio:\n"))
                    rad = r*r*pi
                    print("El Resultado es:\n",rad ,''+'centimetros cuadrados') 
                                                      
                case 2:
                    alt=0
                    base=0
                    res=0
                    print("C A L C U L O   D E L   A R E A   D E   U N   R E C T A N G U L O\n")
                    print("Formula: Area= Altura * Base \n")
                    alt = float(input("Dame la altura \n"))
                    base = float(input("Dame la base \n"))
                    res= base*alt
                    print(f"El resultado es:\n",res, ''+'Centimetros Cuadrados')          
                
                case 3:
                    base=0
                    alt=0
                    res=0
                    print("C A L C U L O   D E L   A R E A   D E   U N   T R I A N G U L O   E Q U I L A T E R O\n")
                    print("Formula: Base * Altura / 2 \n")
                    base=float(input("Dame la base:\n"))
                    alt=float(input("Dame la altura:\n"))
                    res = base*alt/2
                    print("El area del Triangulo Equilatero es:\n",res,''+'Centimetros Cuadrados')
                
                case 4:
                    lado = 0
                    print("C A L C U L O   D E L   A R E A   D E  U N  C U A D R A D O\n")
                    print("Formula: Area = Lado * Lado\n")
                    lado = float(input("Dame el Lado:\n"))
                    res=lado*lado
                    print("El Area del Cuadrado es: \n",res,''+"centimetros Cuadrados")
                           
                case 5:
                    S = str(input("Estas Seguro de Salir Si/No:"))
                    if S == "Si":
                        print("Hasta Luego Gracias\n")
                        break

    
                            
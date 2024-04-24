while True:
        try:
            Nombre = str( input("Dame el Nombre del Paciente: "))
            b
            reak
        except ValueError:
            print("Introduciste un Valor erroneo intentalo de nuevo")    
while True:
        try:
            ApellidoPaterno = str (input("Dame el Apellido Paterno: "))
            break
        except ValueError:
            print("Introciste un valor erroneo intentalo de nuevo")
while True:
            try:                
                ApellidoMaterno = str(input("Dame le Apellido Madsterno: "))
                break
            except ValueError:
                print("Introduciste un valor erroneo intentalo de nuevo")    
while True:
    try:
        Edad = int(input("Dame la Edad del Paciente: "))
        break
    except (ValueError,TypeError,IndexError,NameError):
        print("Introduciste Un Valor Erroneo ingresa numeros enteros y Decimales")
while True:
    try:
        Peso = float(input("Dame el Peso del Paciente :"))
        break
    except ValueError:
        print("Introduciste Un dato Erroneo solo puedes introducir valores numericos y decimales ")
while True:
    try:    
        Estatura = float(input("Dame la Estatura del Paciente:"))
        break
    except ValueError:
        print("Introduciste un Valor Erroneo solo puedes introducir valores Numericos y decimales")

IMC = Peso/Estatura**2
IMC2 = round(IMC,2)
print("LA INFORMACION DEL PACIENTE YA CON SU IMC CALCULADO ES:\n\n")
print("El nombre del Paciente es: ", Nombre)
print("El Apellido Paterno del Paciente es:", ApellidoPaterno)
print("El Apellido Materno del Paciente es:",ApellidoMaterno)
print("La Edad del Paciente es:",Edad)
print("El Peso del Paciente es:",Peso)
print("La Estatura del Paciente es:", Estatura)
print("El Indice de Masa Corporal es:", IMC2)

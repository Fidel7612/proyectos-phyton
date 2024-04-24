while True:    
            try:
                AñoActual = int(input("Introduce el Año actual:"))
                break
            except ValueError:
                print("Introduciste un error Introduce la fecha actual")
while True:
            try:
                 AñoAComparar = int(input("Introduce el Año a Comparar:"))
                 break
            except ValueError:
                            print("Introduciste una error. Introduce el año a Comparar")
if AñoAComparar == 2022:
    AñoActual = AñoActual-AñoAComparar 
    print("Ha pasado solo",AñoActual,"año desde el año actual")
elif AñoAComparar == 2024:
     AñoAComparar=AñoAComparar-AñoActual
     print("Falta",AñoAComparar,"para llegar a esa fecha que introduciste")
elif AñoAComparar<AñoActual:
    AñoActual = AñoActual-AñoAComparar
    print("Han pasado desde la fecha que introduciste:",AñoActual, "Años" )
elif AñoAComparar>AñoActual:
     AñoAComparar=AñoAComparar-AñoActual
     print("Para llegar a la fecha que introduciste faltan",AñoAComparar ,"años")
elif AñoAComparar == AñoActual:
     print("Introduciste la misma fecha el año",AñoAComparar)

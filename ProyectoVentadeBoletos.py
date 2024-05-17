# En un Concierto de Musica se pretende llevar a cabo para un evento
# caridad para obras de beneficiencia, para personas enfermas de cancer
# el evento se llevara a cabo el dia 31 de enero del 2024, se pretende
# llevar a cabo en el estadio Azteca  tomando en cuenta que para cada zona
# se dara un precio diferente los cuales son:
#1.- Zona A: Costo de boleto es de : $250.00 por persona
#2.- Zona B: Costo de Boleto es: $300.00 por persona
#3.- Zona C: Costo de boleto es: $350.00 por persona
#4.- Zona Palcos: Costo del Palco: $2500.00 para 6 personas
# se debera imprimir el total del costo de los boletos y si se paga con 
# tarjeta llevara un cargo del 10% del total
print("---------------M E N U ----------------")
print("1.- Precio del boleto Zona A: $250 por persona")
print("2.- Precio del boleto Zona B: $300 por Persona")
print("3.- Precio del boleto Zona C: $350 por persona")
print("4.-Precio del Palco: $2500")
print("5.- Costo Total de Los Boletos")
print("6.- Nuevo Cliente")
print("7.- Salir ")
i = 1
print("Su numero de Folio es:", i)
while True:
            op = int(input("Elige Una Opcion: "))            
            match  op:
                case 1:
                    numboletos = int(input("Cuantos Boletos Deseas Comprar En Zona A:"))
                    total = numboletos * 250
                    print("El Costo total de los" , numboletos ,"boletos es de: $" , total)
                case 2:
                    numboletos2 = int(input("Cuantos Boletos Deseas Comprar en Zona B:"))
                    total2 = numboletos2 * 300
                    print("El Costo Total de los" , numboletos2 ,"boletos es de: $", total2)
                case 3:
                    numboletos3 = int(input("Cuantos Boletos Deseas Comprar en la Zona C:"))
                    total3 = numboletos3 * 350
                    print("El Costo total de los ", numboletos3, "boletos es de: $", total3)
                case 4:
                    numboletos4 = int(input("Dame el Numero de Palcos que DESEAS comprar:"))
                    total4 = numboletos4 * 2500
                    print("El Costo total del numero de palcos ", numboletos4, "es de: $ ", total4)
                case 5:
                    print("Como desea pagar:")
                    print("1.- Efectivo")
                    print("2.- Con tarjeta")
                    pago = float(input("Elige una opcion  "))
                    if pago == 2:
                        pagototal = total + total2 + total3 + total4 
                        pagototal2 = pagototal * 0.10 
                        pagototal3 = pagototal2 + pagototal
                        print("Su numero de Folio es:",i)
                        print("Total es de: $ ",pagototal ," El cargo del 10 porciento es: $",pagototal2, "El total ya con el Cargo es: $",pagototal3)                        
                    else:
                        pagototal = total + total2 + total3 + total4
                        print("Su Numero de Folio es: ",i) 
                        print("El pago total Sin Cargo de Tarjeta es: $",pagototal)
                case 6:
                    i=1+i 
                       
                case 7:
                    salir = str(input("Estas Seguro que deseas Salir Si/No\n"))
                    if salir == "No":
                        pass               
                    else:
                        i = 1 + i
                        break
                        
def promedio(*numeros):
    promedio = sum(numeros)/len(numeros)
    print("El promedio es:", promedio)

    promedio(4)
    promedio(4, 5, 6)
    promedio(1, 2, 3, 4, 5, 6, 7, 8, 9)
    
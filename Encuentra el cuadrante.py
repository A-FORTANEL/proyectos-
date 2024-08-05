# Programa Encuentra el cuadrante

# Solicita al usuario que ingrese las coordenadas del punto
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

# Verifica que ninguna coordenada sea 0
if x == 0 or y == 0:
    print("Las coordenadas no deben ser 0.")
else:
    # Identifica el cuadrante en base a los valores de X y Y
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV")

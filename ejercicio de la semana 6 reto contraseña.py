# Contraseña predeterminada
Pass = "43BN"
cont = 1

# Solicita al usuario que ingrese la contraseña
nombre = input("Ingresa tu contraseña: ")

# Bucle que permite hasta 3 intentos
while cont <= 3:
    if nombre == Pass:
        print("Bienvenido, Contraseña correcta.")
        break
    else:
        if cont < 3:
            nombre = input("Contraseña incorrecta, intenta nuevamente: ")
        else:
            print("Has excedido el número de intentos permitidos.")
    cont += 1
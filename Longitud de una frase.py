# Programa para verificar la Longitud de una frase

# Solicita al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Calcula la longitud de la palabra
longitud = len(palabra)

# Verifica si la longitud está en el rango de 4 a 8 letras
if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")

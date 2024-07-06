# proyectos-
calculadora IMC
def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def main():
    print("Programa para calcular el Índice de Masa Corporal (IMC)\n")

    # Datos del usuario (coloca tus datos aquí)
    nombre = "Jose Arturo"
    apellido_paterno = "Fortanel"
    apellido_materno = "Gonzalez"
    edad = 36
    peso = 73
    estatura = 1.70

    # Calcular IMC
    imc = calcular_imc(peso, estatura)

    # Mostrar resultados
    print("\nDatos personales:")
    print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")

    # Clasificación del IMC
    if imc < 18.5:
        print("Estado: Bajo peso")
    elif imc < 24.9:
        print("Estado: Peso normal")
    elif imc < 29.9:
        print("Estado: Sobrepeso")
    elif imc < 34.9:
        print("Estado: Obesidad tipo I")
    elif imc < 39.9:
        print("Estado: Obesidad tipo II")
    else:
        print("Estado: Obesidad tipo III (mórbida)")

if __name__ == "__main__":
    main()

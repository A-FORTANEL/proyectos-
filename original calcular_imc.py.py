# calcular_imc
def calcular_imc():
        # Datos específicos proporcionados
        nombre = "Jose Arturo Fortanel Gonzalez"
        edad = 36
        altura = 1.70  # en metros
        masa = 73  # en kg

        # Calculo del IMC, masa (en kilogramos) entre la estatura (en metros) elevada al cuadrado
        IMC = masa / (altura ** 2)

        # Determinamos si la persona es menor o mayor de edad
        if edad < 18:
            print(f"{nombre}, usted es menor de edad.")
        else:
            print(f"{nombre}, usted es mayor de edad.")
        
        # Mostramos el valor del IMC
        print(f"Su IMC es: {IMC:.2f}")

        # Hacemos las distintas validaciones del IMC y mostramos la clasificación correspondiente
        if IMC < 16.00:
            print("Delgadez severa")
        elif IMC < 17.00:
            print("Delgadez moderada")
        elif IMC < 18.50:
            print("Delgadez leve")
        elif IMC < 25.00:
            print("Normal")
        elif IMC < 30.00:
            print("Sobrepeso")
        elif IMC < 35.00:
            print("Obesidad leve")
        elif IMC < 40.00:
            print("Obesidad media")
        else:
            print("Obesidad mórbida")

if __name__ == "__main__":
    calcular_imc()

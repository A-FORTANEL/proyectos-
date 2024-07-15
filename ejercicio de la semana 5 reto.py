# Saludo al usuario y descripción del programa
print("calcular los años trasncuerridos entre 2 años.\n")

# Función solicitar un año y validarlo
def obtener_año(mensaje):
    while True:
        try:
            # Solicita el año al usuario
            año = int(input(mensaje))
            # Valida que el año sea mayor a cero y tenga cuatro dígitos
            if año <= 0 or len(str(año)) != 4:
                print("El año debe ser un número válido de cuatro dígitos (YYYY).")
            else:
                return año  # Devuelve el año si es válido
        except ValueError:
            # Maneja el caso en que se ingresan caracteres no numéricos
            print("Por favor, ingresa solo números.")

# Función para calcular la diferencia entre dos años
def calcular_diferencia(año_actual, año_final):
    # Compara los años y genera un mensaje correspondiente
    if año_actual == año_final:
        return f"Has ingresado el mismo año, estamos en el año {anio_actual}."
    elif año_actual > año_final:
        años_pasados = año_actual - año_final
        return f"Hace {años_pasados} año(s) desde {año_final} hasta {año_actual}."
    else:
        años_futuros = año_final - año_actual
        return f"Faltan {años_futuros} año(s) para llegar al {año_final} desde {año_actual}."

# Función principal
def main():
    # Obtiene el año actual
    año_actual = obtener_año("Ingresa el año actual (YYYY): ")
    # Obtiene el año final
    año_final = obtener_año("Ingresa el año final (YYYY): ")

    # Calcula la diferencia y muestra el resultado
    resultado = calcular_diferencia(año_actual, año_final)
    print("\n" + resultado)

# Ejecuta la función principal
if __name__ == "__main__":
    main()

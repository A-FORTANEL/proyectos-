import numpy as np
import matplotlib.pyplot as plt

def simulate_galton(num_balls, num_levels):
    bins = np.zeros(num_levels * 2 + 1, dtype=int)

    for _ in range(num_balls):
        position = num_levels
        for _ in range(num_levels):
            position += np.random.choice([-1, 1])
        if 0 <= position < len(bins):
            bins[position] += 1

    return bins

def plot_histogram(data):
    plt.bar(range(len(data)), data, color='blue', edgecolor='black')
    plt.xlabel('Contenedor')
    plt.ylabel('Número de Canicas')
    plt.title('Distribución de Canicas en la Máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_balls = 3000
num_levels = 12

# Ejecutar la simulación
results = simulate_galton(num_balls, num_levels)

# Graficar los resultados
plot_histogram(results)

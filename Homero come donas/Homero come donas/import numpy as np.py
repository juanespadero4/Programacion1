import numpy as np

def generar_matriz_aleatoria():
    return np.random.randint(1, 10, size=(3, 3))

matriz = generar_matriz_aleatoria()
print(matriz)
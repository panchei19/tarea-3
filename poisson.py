import matplotlib.pyplot as cajas
from scipy.stats import poisson
import numpy as np

lambda_poisson = 30
tamaños = [10**2, 10**3, 10**4, 10**5]
poissons = []

for size in tamaños:
    unpoisson = poisson.rvs(lambda_poisson, size=size)
    poissons.append(unpoisson)
    media= np.mean(unpoisson)
    varianza=np.var(unpoisson)
    print(f"Varianza para tamaño {size}: {varianza}")
    print(f"Media para tamaño {size}: {media}")


cajas.figure(figsize=(12, 8))
cajas.boxplot(poissons, labels=["10^2", "10^3", "10^4", "10^5"])
cajas.title("Distribución Poisson\nλ = 30")
cajas.xlabel("Tamaño")
cajas.ylabel("Valores")
cajas.show()


cajas.figure(figsize=(12, 8))
for i, sample in enumerate(poissons):
    cajas.subplot(2, 2, i+1)
    cajas.hist(sample, bins=30, alpha=0.7)
    cajas.title(f"Distribución de Poisson\nTamaño de Muestra = 10^{i+2}")
    cajas.xlabel("Valores")
    cajas.ylabel("Frecuencia")
cajas.tight_layout()
cajas.show()


def calcular_mediana(unpoisson):
    poissonordenados = sorted(unpoisson)
    n = len(unpoisson)
    mid = n // 2

    if n % 2 == 0:
        return (poissonordenados[mid - 1] + poissonordenados[mid]) / 2
    else:
        return poissonordenados[mid]


def calcular_moda(unpoisson):
    frecuencia = {}
    for num in unpoisson:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1

    max_frecuencia = max(frecuencia.values())
    modas = [key for key, value in frecuencia.items() if value ==
             max_frecuencia]
    return modas[0]


medianas_poisson = []
modas_poisson = []


print("Medianas Poisson:", medianas_poisson)
print("Modas Poisson:", modas_poisson)

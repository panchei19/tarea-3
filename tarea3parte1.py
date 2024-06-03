import matplotlib.pyplot as cajas 
from scipy.stats import binom

n = 100
p = 0.35

tamaños = [10**2, 10**3, 10**4, 10**5]
binomios = []

for size in tamaños:
    binomio = binom.rvs(n, p, size=size)
    binomios.append(binomio)

cajas.figure(figsize=(12, 8))
cajas.boxplot(binomios,  labels =["10^2", "10^3", "10^4", "10^5"])
cajas.title("Diagramas de Cajas")
cajas.xlabel("Tamañ0")
cajas.ylabel("Valor")
cajas.show()
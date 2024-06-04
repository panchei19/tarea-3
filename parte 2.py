import matplotlib.pyplot as cajas 
from scipy.stats import geom

p_geom = 0.08

tamaños = [10**2, 10**3, 10**4, 10**5]
geometricos = []

for size in tamaños:
    geo = geometricos.rvs(p_geom, size=size)
    geometricos.append(geo)

cajas.figure(figsize=(12, 8))
cajas.boxplot(geometricos,  labels =["10^2", "10^3", "10^4", "10^5"])
cajas.title("Diagramas de Cajas")
cajas.xlabel("Tamañ0")
cajas.ylabel("Valor")
cajas.show()

from math import hypot
adj = float(input('digite a medida do cateto adjacente:'))
ops = float(input('digite a medida do cateto oposto: '))
hip = hypot(adj, ops)
print('O calculo de hipotenusa é igual à {:.2f}'.format(hip))
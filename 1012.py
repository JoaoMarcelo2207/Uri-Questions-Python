a, b, c = input().split(" ")

areatr = ((float(a)*float(c))/2)
areac = 3.14159 * float(c)**2
areatp = ((float(a)+float(b))*float(c))/2
areaq = float(b)**2
arear = float(a)*float(b)

print('TRIANGULO: {:.3f}'.format(areatr))
print('CIRCULO: {:.3f}'.format(areac))
print('TRAPEZIO: {:.3f}'.format(areatp))
print('QUADRADO: {:.3f}'.format(areaq))
print('RETANGULO: {:.3f}'.format(arear))
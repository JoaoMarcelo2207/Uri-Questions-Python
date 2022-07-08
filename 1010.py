cp1, np1, vp1 = input().split(" ")
cp2, np2, vp2 = input().split(" ")

val = (float(np1)*float(vp1)) + (float(np2)*float(vp2))

print('VALOR A PAGAR: R$ {:.2f}'.format(val))
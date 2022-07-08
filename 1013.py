a, b ,c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

maiorab = int(((a + b+ abs(a-b))/2))
maiort = int(((c + maiorab + abs(c-maiorab))/2))
print(maiort, 'eh o maior')

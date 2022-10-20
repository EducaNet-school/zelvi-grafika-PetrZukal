#FIBONACCIHO RADA

print("Fibonacciho rada")
seznam = [0, 1]
seznam2 = [0, 1]

#zadavani hodnoty

print("Zadejte hodnotu")
cisla = int(input())

#pocitani 2

for cisla2 in range(cisla-2):
    cisla2 = seznam[seznam2[0]] + seznam[seznam2[1]]
    seznam2[0] += 1
    seznam2[1] += 1
    seznam.append(cisla2)

#vysledek

else:
    print("VYSLEDEK")
print(seznam)

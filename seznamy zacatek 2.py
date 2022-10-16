
print ("Malá násobilka")

cislo = int(input("Zadejte číslo které bude od 2 do 10:"))

if cislo <11 and cislo >=2:
    for j in range(2,11):
        print(cislo, 'x', j, '=', cislo*j)

else:
    print("Zkus to znovu")

#pekny format print
print("Zadejte liché číslo do 9")

cislo = int(input())
if cislo % 2 == 0:
    cislo += 1


sez = [cislo]

for i in range(9):
    cislo+= 2

else:
    print("Zkus to znovu")
print(sez)

# ten else radek 13 nechapu
# mel se pocitat prumer
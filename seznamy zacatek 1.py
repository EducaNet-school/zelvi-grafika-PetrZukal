prvnicislo = int(input("Zadejte vase prvni cislo"))
poslednicislo = int(input("Zadejte vase posledni cislo"))

if prvnicislo<poslednicislo:
    for cislo in range(prvnicislo, poslednicislo +1):
        if cislo % 2 != 0:
            print(cislo, end = "")
else:
    print("Zkus to znovu")

#ta cisla tiskni s mezerou, nejsou to prvocisla, neukladas do seznamu
# pekna kontrola uzivatelskeho vstupu



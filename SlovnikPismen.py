
Text = input("Zadejte slovo")

Abeceda = ['a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,']

abeceda1 = {}

for Text in Text:
    if Text in Abeceda:

        abeceda1[Text] += 1

    else:
        abeceda1[Text] = 1

print(abeceda1)





x = int(input("Dati numarul de pasari: "))
if (x % 2 == 0):
    nr_g = x // 2
    nr_r = nr_g // 4
    nr_gaste = x - nr_g - nr_r
    print(nr_g, "gaini")
    print(nr_r, "rate")
    print(nr_gaste, "gaste")
else:
    print("Dati un numar par")
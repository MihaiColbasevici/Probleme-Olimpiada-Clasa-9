x = int(input("Dați numărul de păsări: "))
if (x % 2 == 0):
    nr_g = x // 2
    nr_r = nr_g // 4
    nr_gaste = x - nr_g - nr_r
    print(nr_g, "găini")
    print(nr_r, "rațe")
    print(nr_gaste, "gâște")
else:
    print("Dați un număr par")

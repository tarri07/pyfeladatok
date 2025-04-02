def ket_szam_kozott():
    print("2. feladat: Két szám között")
    szám1 = int(input("Írd be az első számot: "))
    szám2 = int(input("Írja be a második számot: "))

    if szám1 > szám2:
        szám1, szám2 = szám2, szám1

    számok = list(range(szám1, szám2 + 1))
    
    print("Az alábbi számokat találtam:", end=" ")
    print(*számok, sep=", ")

    osztható3 = sum(1 for num in számok if num % 3 == 0)
    print(f"A két szám között {osztható3} db szám van, ami osztható 3-mal!")

ket_szam_kozott()
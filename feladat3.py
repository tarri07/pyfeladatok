fajl = open("legmagasabb.txt", "r", encoding="utf-8")
sorok = fajl.readlines()
fajl.close()

épület_lista = []

for sor in sorok[1:]:
    adat_részek = sor.strip().split(";")
    
    épület_adat = {
        "név": adat_részek[0],
        "város": adat_részek[1],
        "ország": adat_részek[2],
        "magasság": float(adat_részek[3]),
        "emeletek_száma": int(adat_részek[4]),
        "építés_éve": int(adat_részek[5])
    }
    
    épület_lista.append(épület_adat)

épületek_száma = len(épület_lista)
print(f"3.2 feladat: Épületek száma: {épületek_száma} db")

összes_emelet = 0
for épület in épület_lista:
    összes_emelet += épület["emeletek_száma"]
print(f"3.3 feladat: Emeletek összege: {összes_emelet}")

legmagasabb_épület = épület_lista[0]
for épület in épület_lista:
    if épület["magasság"] > legmagasabb_épület["magasság"]:
        legmagasabb_épület = épület

print("3.4 feladat: A legmagasabb épület adatai")
print(f"Név: {legmagasabb_épület['név']}")
print(f"Város: {legmagasabb_épület['város']}")
print(f"Ország: {legmagasabb_épület['ország']}")
print(f"Magasság: {legmagasabb_épület['magasság']} m")
print(f"Emeletek száma: {legmagasabb_épület['emeletek_száma']}")
print(f"Építés éve: {legmagasabb_épület['építés_éve']}")

van_olasz = False
for épület in épület_lista:
    if épület["ország"] == "Olaszország":
        van_olasz = True
        break

if van_olasz:
    print("3.5 feladat: Van olasz épület az adatok között!")
else:
    print("3.5 feladat: Nincs olasz épület az adatok között.")
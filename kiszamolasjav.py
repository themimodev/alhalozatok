ipCim=input("Add meg a hálózat első három számát (pl. 192.168.10): ")
blokk=32
kezdoHalozat=0
hanyadikHalozat=1
darabHalo=int(input("Hány hálózatot szeretnél? "))

szekreny = []

while hanyadikHalozat <= darabHalo:
    gepekSzama=int(input(f"Hány gépet szeretnél a {hanyadikHalozat}. hálózatnak? "))

    szekreny.append(gepekSzama)

    kezdoHalozat+=blokk
    hanyadikHalozat+=1

szekreny.sort(reverse=True)
print(szekreny)
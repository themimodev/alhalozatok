ipCim=input("Add meg a hálózat első három címét (pl. 192.168.10): ")
hanyadikHalozat=1
darabHalo=int(input("Hány hálózatot szeretnél létrehozni (db)? "))

szekreny=[]

while hanyadikHalozat <= darabHalo:
    gepekSzama=int(input(f"Hány gépet szeretnél a {hanyadikHalozat}. hálózatnak? "))

    hanyadikHalozat += 1

    szekreny.append(gepekSzama)

szekreny.sort(reverse=True)
print(f"Csökkenő sorrendben: {szekreny}")

fiokokSorszama=0
indulo=0

while fiokokSorszama < darabHalo:
    halozat = szekreny[fiokokSorszama] + 2
    fiokokSorszama+=1


    if halozat <= 1:
        blokk = 1
        hely = 8
    elif halozat <= 2:
        blokk = 2
        hely = 7
    elif halozat <= 4:
        blokk = 4
        hely = 6
    elif halozat <= 8:
        blokk = 8
        hely = 5
    elif halozat <= 16:
        blokk = 16
        hely = 4
    elif halozat <= 32:
        blokk = 32
        hely = 3
    elif halozat <= 64:
        blokk = 64
        hely = 2
    elif halozat <= 128:
        blokk = 128
        hely = 1
    else:
        print("Ennyi gép nem fér egy /24-es hálózatba.")
        exit()

    maszk = 256 - blokk
    if indulo+blokk>256:
        print("Ennyi gép nem fér egy /24-es hálózatba.")
        exit()

    print()
    print(f"A(z) {fiokokSorszama}. hálózat számítása: ")
    print(f"Blokk: {blokk}")
    print(f"Maszk: 255.255.255.{maszk}")
    print(f"Hálózati cím: {ipCim}.{indulo}/{24 + hely}")
    print(f"Első gép címe: {ipCim}.{indulo + 1}")
    print(f"Utolsó gép címe: {ipCim}.{indulo + blokk - 2}")
    print(f"Szórási cím: {ipCim}.{indulo + blokk - 1}")

    indulo+=blokk



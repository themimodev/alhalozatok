ipCim=input("Add meg a hálózat első három számát (pl. 192.168.10): ")
gepekSzama=int(input("Hány gépet szeretnél az első hálózatnak? "))

halozat=gepekSzama+2

if halozat<=1:
    blokk=1
    hely=8
elif halozat<=2:
    blokk=2
    hely=7
elif halozat<=4:
    blokk=4
    hely=6
elif halozat<=8:
    blokk=8
    hely=5
elif halozat<=16:
    blokk=16
    hely=4
elif halozat<=32:
    blokk=32
    hely=3
elif halozat<=64:
    blokk=64
    hely=2
elif halozat<=128:
    blokk=128
    hely=1
else:
    print("Ennyi gép nem fér egy /24-es hálózatba.")
    exit()

maszk=256-blokk

print(f"Blokk: {blokk}")
print(f"Maszk: 255.255.255.{maszk}")
print(f"Prefix: {ipCim}.0/{24+hely}")

indulo=0

print(f"Hálózati cím: {ipCim}.{indulo}")
print(f"Első gép címe: {ipCim}.{indulo+1}")
print(f"Utolsó gép címe: {ipCim}.{indulo+blokk-2}")
print(f"Szórási cím: {ipCim}.{indulo+blokk-1}")

masodikindulo= indulo + blokk

gepekSzama=int(input("Hány gépet szeretnél a második hálózatnak? "))

halozat=gepekSzama+2

if halozat<=1:
    blokk=1
    hely=8
elif halozat<=2:
    blokk=2
    hely=7
elif halozat<=4:
    blokk=4
    hely=6
elif halozat<=8:
    blokk=8
    hely=5
elif halozat<=16:
    blokk=16
    hely=4
elif halozat<=32:
    blokk=32
    hely=3
elif halozat<=64:
    blokk=64
    hely=2
elif halozat<=128:
    blokk=128
    hely=1
else:
    print("Ennyi gép nem fér egy /24-es hálózatba.")
    exit()

maszk=256-blokk

print(f"Blokk: {blokk}")
print(f"Maszk: 255.255.255.{maszk}")
print(f"Prefix: {ipCim}.{masodikindulo}/{24 + hely}")

print(f"Hálózati cím: {ipCim}.{masodikindulo}")
print(f"Első gép címe: {ipCim}.{masodikindulo + 1}")
print(f"Utolsó gép címe: {ipCim}.{masodikindulo + blokk - 2}")
print(f"Szórási cím: {ipCim}.{masodikindulo + blokk - 1}")

harmadikindulo= masodikindulo + blokk

gepekSzama=int(input("Hány gépet szeretnél a harmadik hálózatnak? "))

halozat=gepekSzama+2

if halozat<=1:
    blokk=1
    hely=8
elif halozat<=2:
    blokk=2
    hely=7
elif halozat<=4:
    blokk=4
    hely=6
elif halozat<=8:
    blokk=8
    hely=5
elif halozat<=16:
    blokk=16
    hely=4
elif halozat<=32:
    blokk=32
    hely=3
elif halozat<=64:
    blokk=64
    hely=2
elif halozat<=128:
    blokk=128
    hely=1
else:
    print("Ennyi gép nem fér egy /24-es hálózatba.")
    exit()

maszk=256-blokk

print(f"Blokk: {blokk}")
print(f"Maszk: 255.255.255.{maszk}")
print(f"Prefix: {ipCim}.{harmadikindulo}/{24 + hely}")

print(f"Hálózati cím: {ipCim}.{harmadikindulo}")
print(f"Első gép címe: {ipCim}.{harmadikindulo + 1}")
print(f"Utolsó gép címe: {ipCim}.{harmadikindulo + blokk - 2}")
print(f"Szórási cím: {ipCim}.{harmadikindulo + blokk - 1}")


def funksiya(*test):
    for i in test:
        print(i)
funksiya("elshodbek", "ali", "vali", "jafar")
import random

son = random.randint(1, 100)
urinish = 0

print("🎮 SONNI TOPISH O'YINIGA XUSH KELIBSIZ!")
print("Men 1 dan 100 gacha son o'yladim.")

while True:
    taxmin = int(input("Sonni kiriting: "))
    urinish += 1

    if taxmin > son:
        print("⬇️ Kichikroq son kiriting!")

    elif taxmin < son:
        print("⬆️ Kattaroq son kiriting!")

    else:
        print("🎉 TABRIKLAYMAN! TO'G'RI TOPDINGIZ!")
        print("Urinishlar soni:", urinish)
        break

print("\nO'yin tugadi!")

for i in range(1, 6):
    print("Rahmat! ❤️")
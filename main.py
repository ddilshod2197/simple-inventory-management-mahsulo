class Mahsulot:
    def __init__(self, nom, miqdor, narx):
        self.nom = nom
        self.miqdor = miqdor
        self.narx = narx

class Ombor:
    def __init__(self):
        self.mahsulotlar = {}

    def qo'sh(self, mahsulot):
        if mahsulot.nom in self.mahsulotlar:
            self.mahsulotlar[mahsulot.nom].miqdor += mahsulot.miqdor
        else:
            self.mahsulotlar[mahsulot.nom] = mahsulot

    def o'zgartir(self, nom, miqdor):
        if nom in self.mahsulotlar:
            self.mahsulotlar[nom].miqdor = miqdor
        else:
            print("Bunday mahsulot yo'q")

    def ko'rsat(self):
        for mahsulot in self.mahsulotlar.values():
            if mahsulot.miqdor < 10:
                print(f"{mahsulot.nom} - {mahsulot.miqdor} dona")

    def yetarli_emas(self):
        for mahsulot in self.mahsulotlar.values():
            if mahsulot.miqdor < 10:
                return True
        return False

ombor = Ombor()

while True:
    print("1. Mahsulot qo'shish")
    print("2. Mahsulot o'zgartirish")
    print("3. Mahsulot ko'rsatish")
    print("4. Yetarli emas mahsulotlar ko'rsatish")
    print("5. Omborni yangilash")
    print("6. Chiqish")

    savol = input("Savolni tanlang: ")

    if savol == "1":
        nom = input("Mahsulot nomi: ")
        miqdor = int(input("Mahsulot miqdori: "))
        narx = int(input("Mahsulot narxi: "))
        mahsulot = Mahsulot(nom, miqdor, narx)
        ombor.qo'sh(mahsulot)
    elif savol == "2":
        nom = input("Mahsulot nomi: ")
        miqdor = int(input("Mahsulot miqdori: "))
        ombor.o'zgartir(nom, miqdor)
    elif savol == "3":
        ombor.ko'rsat()
    elif savol == "4":
        if ombor.yetarli_emas():
            print("Yetarli emas mahsulotlar mavjud")
        else:
            print("Yetarli emas mahsulotlar yo'q")
    elif savol == "5":
        ombor.mahsulotlar.clear()
    elif savol == "6":
        break
    else:
        print("Savolni tanlang")

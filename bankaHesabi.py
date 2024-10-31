class BankaHesabi:
    def __init__(self,hesapNumarasi,bakiye=0):
        self.hesapNumarasi=hesapNumarasi
        self.bakiye=bakiye
    def paraYatir(self,miktar):
        self.bakiye+=miktar
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye}TL")
    def paraCek(self,miktar):
        if miktar>self.bakiye:
            print("Yetersiz bakiye")
        else:
            self.bakiye-=miktar
            print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye}TL")
    def bakiyeGoster(self):
        print(f"Hesap{self.hesapNumarasi} bakiyesi:{self.bakiye} TL")

hesaplar={}
while True:
    print("1. Hesap Oluştur")
    print("2. Para Yatır")
    print("3. Para Çek")
    print("4. Bakiyeyi Göster")
    print("5. Çıkış")

    secim=int(input("Bir seçenek seçin:"))

    if secim==1:
        hesapNumarasi=input("Hesap numarasını girin:")
        if hesapNumarasi in hesaplar:
            print("Hesap zaten mevcut")
        else:
            hesaplar[hesapNumarasi]=BankaHesabi(hesapNumarasi)
            print(f"Hesap {hesapNumarasi} oluşturuldu")
    elif secim==2:
        hesapNumarasi=input("Hesap numarasını giriniz:")
        if hesapNumarasi in hesaplar:
            miktar=float(input("Yatırılacak miktarı girin:"))
            hesaplar[hesapNumarasi].paraYatir(miktar)
        else:
            print("Hesap bulunamadı")
    elif secim==3:
        hesapNumarasi=input("Hesap numarasını giriniz:")
        if hesapNumarasi in hesaplar:
            miktar=float(input("Çekilecek miktarı girin:"))
            hesaplar[hesapNumarasi].paraCek(miktar)
        else:
            print("Hesap bulunamadı")
    elif secim==4:
        hesapNumarasi=input("Hesap numarasını giriniz:")
        if hesapNumarasi in hesaplar:
            hesaplar[hesapNumarasi].bakiyeGoster()
        else:
            print("Hesap bulunamadı")
    elif secim==5:
        break
    else:
        print("Geçersiz Seçim")
        

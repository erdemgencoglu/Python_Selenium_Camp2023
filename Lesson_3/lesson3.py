
# Type Casting
# int(),str(),float()

vade = input("Lutfen istediginiz vade sayisini giriniz: ")
print(type(vade))
# print(vade+1) #Type error
print(int(vade)+12)

faiz = int(input("Faiz oranını giriniz: "))
faiz = faiz + 12
print("Seçtiğiniz faiz oranı: "+str(faiz))
print("Seçtiğiniz faiz oranı: {vadeSayisi}".format(vadeSayisi=vade))

isim = "Halit"
metin = "Merhaba {name}".format(name=isim)
print(metin)

metin = f"Hoşgeldiniz {isim}"
print(metin)

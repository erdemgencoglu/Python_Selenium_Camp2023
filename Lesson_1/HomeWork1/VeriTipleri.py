print("-------------Metinler ve metin islemleri-------------")
metin = "Ali ata bak"  # String türünde değişken tanımlama
paragraf = """Birden fazla satira sahip 
strinng ifadeler cift tirnak ile atanabilir"""  # Birden fazla satır

print(metin)
print(paragraf)
print("sonuc1: "+paragraf[0])   # 0. indexdeki karakteri dön
print("sonuc2: "+paragraf[:6])  # 6. index'e kadar olanları seç
print("sonuc3: "+paragraf[6:])  # 6. index'den sonrasını seç
print("sonuc4: "+paragraf[12:22])  # 12 ve 22. index arasındakiler seç
# print("karakter"+123)         # Karakter ve sayı toplamında tip hatası alınır atanan değişken türüne dikkat edilmelidir.
print(len(paragraf))            # len() metin uzunluğunu döndürür
print(metin.lower())            # tüm karakterleri küçültür
print(metin.upper())            # tüm karakterleri büyük hale getiri
print(metin.replace("Ali", "Mehmet"))  # replace istenilen ifadeyi değiştirir
# split() verilen parametreye göre stringi bölmeye yarar sonuç string dizisi olarak geri döner
dizi = metin.split(" ")
print(dizi)
print(metin.strip())            # Başdaki ve sondaki boşluk karakterlerini siler
print(metin.startswith("A"))    # String verilen ifade ile başlıyormu
print(metin.endswith("k"))      # String verilen ifade ile bitiyormu
# String içinde arama yapar bulunan stringin başlangıç indexini döner bulamassa hata döner
print(metin.find("ata"))
# String içinde arama yapar bulunan stringin başlangıç indexini döner bulamassa -1 döner
print(metin.index("ata"))
# Verilen ifadenin kaç kere tekrarlandıpını döner
print(metin.count("a"))
print("-------------Sayılar ve sayı islemleri-------------")
sayi1 = 123     # integer sayı
sayi2 = 12.3    # float sayı
sayi3 = -14     # negative
print(sayi1+sayi2)
print("-------------Mantıksal değişkenler-------------")
isRetailer = False
isSupplier = True
print("-------------Dizi Türleri-------------")
print("--Listeler--")
mylist = ["apple", "banana", "cherry"]
print(mylist)
list2 = ["abc", 34, True, 40, "male"]
print(list2)
print("--Tupple lar--")
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print("--Dictionary--")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["model"])

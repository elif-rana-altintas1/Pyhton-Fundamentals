
#! Değişken (Variable): Uygulama çalıştığı süre zarfında içerisinede değer saklayan ve
#! istediğimiz zaman bu değerlere erişerek kullandığımız yapdırız. Değişken içerisinde tutulan değere erişmek için değişkenin adından onu çağırarak erişebiliyoruz.

#? Değişken Tanımler değişkenime ilk önce bir isim veriyoruz.
#? Matematikte ki tek eşitlik sembolü ile '=' içerisine değer atıyoruz (assigned).
# x: int = 3

# print(x)

#* integer --> pozitif ve negatif tam sayılar için bu değişken tipini kullanıyoruz.
#* string --> bu metinsel ifadeler için kullanılan değişken.

#todo sözel ifadeleri tanımlarken ya tek yada çift tırnak kullanıyoruz.

# first_name = 'Mike Tyson' # first_name değişkeni string tiptedir.
# print(first_name)
# print(type(first_name)) #? burada değişkenimizin tipi str yani string neden çünkü içerisinde Mike Tyson yani sözel bir ifade var


#* Değişken tanımlanırken dikkat edilecek hususlar
#* Değişkenler rakamla başlamamalı
#* Türkçe karakter içermemeli
#* Boşluk barındırmamalı firstName
#* Değişken isimlerini yaptığı işle ilintili olmasını telkin

# first_name = 10

# print(first_name)
# print(type(first_name)) #? burada tipi integer yani tam sayı


#! 2 tane sayıyı toplayıp ekrana yazdıran uyguglamayı yazınız
# sayi_1 = 5
# sayi_2 = 10

# toplam = sayi_1 + sayi_2

# print(toplam)

# #! yukseklik ve taban bilgisi bilinen bir üçgenin alanını hesaplayın
# yukseklik = 10
# taban = 20

# alan = yukseklik * taban / 2

# print(alan)

# #! Kullanıcıdan alınan 2 adet sayıyı çarpan uygulamayı yazınız
# number_1 = int(input('Lütfen sayı giriniz: '))
# number_2 = int(input('Lütfen sayı giriniz: '))
# print(type(number_1))
# carpim = number_1 * number_2

# print(carpim)

# #! Kulanıcıdan alınan kenar bilgisine göre karenin alanını ve çevresini hesaplayan kodu yazınız lütfen
# edge = int(input('Edge: '))

# area = edge * edge
# premiter = 4 * edge

# print(f'Area: {area}')
# print(f'Premiter: {premiter}')

# print('Area', area)
# print('Area: {}'.format(area))

# #! Dikdörtgenin çevresini ve alanını hesaplayın
# kisa_kenar = int(input('Kısa Kenar: '))
# uzun_kenar = int(input('Uzun kenar: '))

# alan = kisa_kenar * uzun_kenar
# cevre = (kisa_kenar + uzun_kenar) * 2

# print(f'Alan: {alan}\nÇevre: {cevre}')


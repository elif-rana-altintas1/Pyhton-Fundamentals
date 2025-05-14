
#!For Loop
#? For loop ile birlikte yoğun olarak kullanılan 2 yapıdır. bunlardan birincisi "in & not in " operatörleri bir diğeri ise range () fonksiyonudur.

#* İn & Not İn

# print ('b' in 'burak')
# print ('B' in 'burak')

# print ('b' not in 'burak')
# print ('B' not in 'burak')
#! NOT: in not in operatörleri if bloklarında kullanılır.

# îf 'b'in 'burak':
#     print(True)
# else:
#     print ( False)


#* Range () fonksiyonu

#* range: içerisine gönderilen değerlere göre bir tam sayı listesi oluşturur.
#* 3 farklı kullanımı mevcuttur
#todo 1. kullanımı : sadece tek değer aldığı senaryo,başlangıç değerini 0 kabul eser bitiş değeri olarak ona verdiğimiz n kabul edersek n-1 kadar bir sayı kümesi oluşturur.
#todo Aşağıdaki örnekte range ile 0 dan başlayan ve 9 a kadar bir sayı aralığı yaratılır.

# for i in range(10): # 0 dan 10 a kadar (10 dahil değil)
#     print(i)

#todo 2. kullanımı range 2 argüman alır. Range (5,10) bu senaryoda başlangıç 5 bitiş 9 olur 

# for i in range(5,10): 
#     print(i, end=',')

#todo 3. kullanım range 3 argüman alır  range(10,100,5) bu senaryoda başlangıç 10 vitiş 99 adım miktarı 5 


# #* örnek:kullanıcıdan başlangıç bitiş ve adım miktarını alalım verilen bilgilere göre ilgili aralıkta kalan sayıların karesini alarak ekrana yazdıralım    
# sayi1 = int(input('başlangıç sayısını giriniz:'))
# sayi2= int (input('bitiş sayısını giriniz:'))
# sayi3= int (input('adım sayısını giriniz:'))
# for i in range (sayi1,sayi2+1,sayi3):
#     print (i*i , end=',')



#* örnek  faktöriyel hesaplama yapınız.


# sayi = int(input("Faktöriyeli alınacak sayıyı girin: "))
# faktoriyel = 1

# if sayi < 0:
#     print("Negatif sayıların faktöriyeli tanımsızdır.")
# elif sayi == 0:
#     print("0! = 1")
# else:
#     for i in range(1, sayi + 1):
#         faktoriyel *= i
#     print(f"{sayi}! = {faktoriyel}")


#* örnek 3 hata alırsak diye düzelt 5t

# try:
#     sayi = int(input("Faktöriyeli alınacak sayıyı girin: "))
#     faktoriyel = 1

#     if sayi < 0:
#         print("Negatif sayıların faktöriyeli tanımsızdır.")
#     elif sayi == 0:
#         print("0! = 1")
#     else:
#         for i in range(1, sayi + 1):
#             faktoriyel *= i
#         print(f"{sayi}! = {faktoriyel}")
# except ValueError as err:  #? aldığımız hata türünü ayıklıyoruz
#     print (err)

#* metnin içinde karakter karakter dolaşmak
# user_name= input('user name:')

# for i in user_name:
#     print(i, end = ',')

#* Örnek : bir kelime olsun kullanıcıdan harf alalım ilgili kelime içerisinde varsa buldunuz yoksa bulamadınız yazsın

# word = 'merhaba burak'
# harf = input("Bir harf girin: ")

# for i in word:
#     if i == harf:
#         print ('buldunuz..!')
#         break
# else:
#     print('bulamadınız..!')

#! not : for fonksiyonuna else yazılabilir.

#! Nested For (iç içe for)


# #?ÇARPIM TABLOSU

# for i in range (1,10):
#     for j in range(1,11):
#         print ( f'{i}x{j}={i*j}')
#     print('=====================')    



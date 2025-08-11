
#! List 
#! Birbirinden farklı değerleri içerisinde depolayan bir yapıdır
#? İndex mekanızması vardır. Yani listenin ilk elemanı 0. indexte tutulur.
#?index pozitif yönde vektörel olarak artan miktarda oluşur.


#* aşağıda bir liste örneği bulunmaktadır.

#boxers = ['mike tyson','muhammed ali','lenox lewis','evander holyfield','george foreman']

#todo bir listenin elemanına onun index bilgisineden erişebilriz

# print(boxers[0]) #output mike tyson
# print(boxers[4]) #output george foreman
# #! Listeler RAM'DE saklanırlar bu yüzden uygulama kapatıldığında liste üzerinde yapılan işlemler silinir.

# #? for loop ile listeler arasında item item dolaşabiliriz.
# for boxer in boxers:
#     print(boxer)

#  #?boxers listesine 'antony jasua' bilgisini ekleyelim.    
#  boxers = ['mike tyson','muhammed ali','lenox lewis','evander holyfield','george foreman']
# degisken = 'antony jasua'
# boxers.append(degisken)
# print(boxers)

#?boxers listesinin 4. indeksine ' deanyony wilder' bilgisini ekleyelim.
# boxers = ['mike tyson','muhammed ali','lenox lewis','evander holyfield','george foreman']
# degisken ='deanyony wilder'
# boxers.insert(4,degisken)
# print(boxers)


#?'antony jasua' listeden silelim.

# boxers = ['mike tyson','muhammed ali','lenox lewis','evander holyfield','george foreman','antony jasua']
# boxers.remove('antony jasua')
# print(boxers)

# #?4. indexte tutulan bilgiyi silelim
# boxers = ['mike tyson','muhammed ali','lenox lewis','evander holyfield','george foreman','antony jasua']
# silinen=boxers.pop(4)
# print(boxers)
# print(silinen)

# #?iki liste birleştirmek için ne yapmalıyız.
# current_boxers = ['mike tyson','muhammed ali','lenox lewis','evander holyfield','george foreman','antony jasua']
# boxers.extend(current_boxers)

###########################################################################################
#* Aşağıda random kütüphanesi içeriisnde bulunan randint fonksiyonunu çalışma sayfamıza ekledik
#?randint fonksiyonu rastgele sayı üretmeye yarar

# # from random import randint

# # *10 tane rasgele sayı üret bunu da boş listeye ekle 
# from random import randint
# sayilar = []
# for i in range(11):
#     rastgele_sayi = randint(0,100)
#     sayilar.append(rastgele_sayi)

# print(sayilar)

#*kullanıcıdan bir söz öbeği alalım.Örneğin 'merhaba ben burak yılmaz'
#*kullanıcıdan alınan bu söz öbeğindeki harflerin hepsini küçük harfe çevirelim
#*ilgili söz öbeğindeki sesli harfler sesli harfler listesine
#*sessiz harfler listesine eklensin

# soz=input('bir söz öbeği girin:').lower()



# sesli_harfler = "aeıioöuü"

# sesliler = []
# sessizler = []

# for harf in soz:
#     if harf in sesli_harfler: 
#       sesliler.append(harf) 
#     else:
#         sessizler.append(harf)

# print("Sesli Harfler:", sesliler)
# print("Sessiz Harfler:", sessizler)

#*rakam, boşluk , soru işareti girilirse karaktere eklensin
#*yol 1 :
# try:
#     soz = input("Bir söz öbeği girin (rakam içermemeli): ").lower()

#     if any(char.isdigit() for char in soz):
#         raise ValueError("Rakam girilmemeli!")

#     sesli_harfler = "aeıioöuü"
#     sesliler = []
#     sessizler = []

#     for harf in soz:
#         if harf.isalpha():  
#             if harf in sesli_harfler and harf not in sesliler:
#                 sesliler.append(harf)
#             elif harf not in sesli_harfler and harf not in sessizler:
#                 sessizler.append(harf)

#     print("Sesli Harfler:", sesliler)
#     print("Sessiz Harfler:", sessizler)

# except ValueError as err:
#     print("Hata:", err)

#*Yol 2 :
# soz=input('bir söz öbeği girin:').lower()



# sesli_harfler = "aeıioöuü"

# sesliler = []
# sessizler = []

# for harf in soz:
#     #todo pyhton içerisinde built-in olarak bulunan bu fonskiyon ilgili harfin a-z yada A-Z aralığında olup olmadığını kontrol eder. şayet ilgili aralıkta ise True döner değilse False döner.

#     if harf.isalpha(): 
#         if harf not in sesliler and harf not in sessizler:
#             if harf in sesli_harfler:
#                 sesliler.append(harf) 
#             else:
#                 sessizler.append(harf)

#     print("Sesli Harfler:", sesliler)
#     print("Sessiz Harfler:", sessizler)

#*rastgele 10 tane sayı üretelim 0 ile 100 arasında olsun. üretilen bu sayıları lst_1 listesine dolduruyoruz. yukarıdaki işlemi lst_2 listesi için yapıyruz 
#*lst_1 ve lst_2'nin indexlerine karşılık gelen değerleri toplayarak gene lst_3 ilgili indexine yazıyoruz
#*tüm soruyu index mantığı kullanarak çözüyoruz (appnend kullanmayınız.)

# from random import randint

# lst_1 = []
# lst_2 = []
# lst_3 = []

# for i in range(10):
#     lst_1.insert(i, randint(0, 100))  # randint() doğru şekilde çağrıldı
#     lst_2.insert(i, randint(0, 100))
#     lst_3.insert(i, lst_1[i] + lst_2[i])

# print(f'1. liste: {lst_1}\n2. liste: {lst_2}\n3. liste: {lst_3}')


#*users =['burak yılmaz' , 'kerim can atlıhan' , 'elif rana esra altıntaş' , 'munzur' ]
#*yukarıdaki  listedeki kullanıcılar için kurumsal mail adresi yaratalım
#*inpur--> burak yılmaz
#*output-->burak.yilmaz@bilgeadam.com gibi

#*YOL 1:
 #users = ['burak yılmaz', 'kerim can atlıhan', 'elif rana esra altıntaş', 'munzur']

# for user in users:
#     # Kullanıcının ismini boşluklara göre ayır
#     parcalar = user.split()
    

#     if len(parcalar) >= 2:
#         ad = parcalar[0]
#         soyad = parcalar[-1]
#         mail = f"{ad}.{soyad}@bilgeadam.com"
#     else:
       
#         mail = f"{parcalar[0]}@bilgeadam.com"
    
#     print(f'{user} -> {mail}')

#*YOL 2:
# mail_adresses=[]
# for user in users:
#     # Kullanıcının ismini boşluklara göre ayır
#     parcalar = user.split()
    
#     mail_adresses=f'{user_names[0]}.{user_names[-1]}@bilgeadam.com'
#     mail_adresses.append(mail_adresses)
#     print(mail_adresses)

#** Munzurun soyadı yok bunu dahil etmeden çözelim.
# users = ['burak yılmaz', 'kerim can atlıhan', 'elif rana esra altıntaş', 'munzur']

# mail_adresses=[]
# for user in users:
#  #Kullanıcının ismini boşluklara göre ayır
#     parcalar = user.split()
#     if len (parcalar)>1:

#         mail_adresses=f'{user_names[0]}.{user_names[-1]}@bilgeadam.com'
#         mail_adresses.append(mail_adresses)
#     print(mail_adresses)


# *users = ['   ipek' , 'burak yılmaz', 'kerim can atlıhan', 'elif rana esra altıntaş', 'munzur']
#*ipek isminindeki boşlukları alma


# mail_adresses = []

# for user in users:
#     user = user.strip()           # Baş/son boşlukları kaldır
#     parcalar = user.split()       # Boşluklardan böl

#     if len(parcalar) > 1:         # En az 2 parça varsa (isim + soyisim)
#         mail = f"{parcalar[0]}.{parcalar[-1]}@bilgeadam.com"
#         mail_adresses.append(mail)

# # Sonuçları yazdır
# for adres in mail_adresses:
#     print(adres)
       

#* users = ['hakan_yılmaz','   ipek' , 'burak yılmaz', 'kerim can atlıhan', 'elif rana esra altıntaş', 'munzur']


# users = ['   ipek', 'burak yılmaz', 'kerim can atlıhan', 'elif rana esra altıntaş', 'munzur', 'hakan_yılmaz']

# mail_adresses = []

# for user in users:
#     user = user.strip()
#     if user.isalpha():
    
#         if len(users) > 1:
#             mail = f"{parcalar[0]}.{parcalar[-1]}@bilgeadam.com"
#             mail_adresses.append(mail)
#     if user.isalpha():


#         print(adres)



#*users = ['hakan yıl_maz','   ipek', 'burak yılmaz', 'kerim can atlıhan', 'elif rana esra altıntaş', 'munzur', 'hakan_yılmaz']

# mail_adresses = []

# for user in users:
#     user_names= user.split(' ') 
#     is_item_consiation =[] 
#     for item in user_names:
#         if item.isalpha():
#             is_item_consiation.append(True)
#         else:
#             is_item_consiation.append(False)    
            
    
#     if len(user_names) > 1:
#         mail = f"{user_names[0]}.{user_names[-1]}@bilgeadam.com"
#         mail_adresses.append(mail)
        
 
###########! ANY

# users = ['hakan yıl_maz','   ipek', 'burak yılmaz', 'kerim can atlıhan', 'elif rana esra altıntaş', 'munzur', 'hakan_yılmaz']
# mail_adresses = []

# for user in users:
#     user_names= user.split(' ') 
#     is_item_consiation =[] 
#     for item in user_names:
#          if item.isalpha():
#             is_item_consiation.append(True)
#          else:
#              is_item_consiation.append(False)    
#     if not any (i is False for i in is_item_consiation):  
      
#         if len(user_names) > 1:
#             mail = f"{user_names[0]}.{user_names[-1]}@bilgeadam.com"
#             mail_adresses.append(mail)



#!!!!! Nested List

# semtler=[
#     ['Sarıyer','Beşiktaş','Ulus'],
#     ['Suadiye','Feneryolu'],
#     ['Bebek', ['Hacıhüsrev','Tarlabaşı']],
#     ['ataköy','Bakırköy','Yeşilköy']
# ]

# print(semtler[0]) #['Sarıyer','Beşiktaş','Ulus']
# print(semtler[0][2]) #Ulus
# print(semtler[2][1][0]) #Hacıhüsrev

#*örnek
# my_family=[
#     ['Burak Yılmaz','beast',36],
#     ['Hakan Yılmaz', 'savage',39],
#     ['İpek Yılmaz','keko',41],
# ]

# for full_name, user_name,age in my_family: #!Kutudan çıkartma 
#     print(f'Full name:{full_name}\nUser Name: {user_name}\nAge: {age}')

#? ÖDEV aşağıdaki listede bulunan kullanıcıların şifrelerini hash'leyerek aynı kullanıcının listesine yazınız 

from hashlib import sha256

users = [
    ['beast', '123'],
    ['savage', '987'],
    ['bear', '578']
]

for username , password in users:
    
    # Şifreyi SHA-256 ile hashle
    hashed_object = sha256(password.encode()) #1 2 3 ü parçaladı
    hashed_password=hashed_object.hexdigest()

    
   
    print(hashed_password)


   

#*YARINA HAZIRLIK 

#? list coprehansion :Python'da daha kısa ve okunabilir şekilde liste oluşturmak için kullanılan bir yapıdır. Döngü (for) ve if gibi ifadeleri tek satıra sığdırır.

#?any() :bir iterable (liste, demet, set, vs.) içindeki en az bir eleman True ise True döner.Hiçbiri True değilse False döner.

#?all() :verilen bir iterable'daki (liste, tuple, set vs.) bütün elemanlar True ise True döner.Eğer bir tanesi bile False ise, sonuç False olur.

#?filter() :bir fonksiyon ve iterable (liste, tuple, vs.) alır.Fonksiyon True döndürdüğü elemanları süzerek geri verir.





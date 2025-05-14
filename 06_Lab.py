
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



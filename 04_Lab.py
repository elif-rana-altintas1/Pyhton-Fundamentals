
#!  Loops (Döngüler)
#? döngüler uygulama içerisinde tekrarlı işlemler yapamıza imkan verirler. 
# Örneğin kullanıcıdan 10 tane sayı alınacak . Bunun için 10 kez çalışacak bir döngü kurulur ve kullanıcıdan 10 tane input tek bir input fonksiyonu ile alınır.

#*iki tip döngümüz var bunlar while loop ve for loop.


#todo while loop
#todo while döngüsünün çalışma prensibi şu şekildedir. bir şart içerir ve sayaç bu şartı sağladığı sürece while loop çalışır. 
# Şart tutmazsa döngü kendisini otomatik olarak break eder.
#sayaç şart doğrultusunda ya arttırılır yada azaltılarak şartın tutup tutmaması her bir adımda kontrol edilir.

#örnek1
#sayac = 0
#while sayac<= 100 : 
 #   print (sayac)
  #  sayac = sayac+1

#region soru-1
#0 ile 100 arasındaki çift sayıları ekrana yazdırın
#counter = 0
#while counter <=100
#print (counter, end='-') #(end yan yana yazmayı sağladı)
#counter=counter+2

#region soru-2
#0 ile 100 arasında kaç tane çift kaç tane tek sayı var yazdıralım

#sayac=0
#cift_sayilar =0
#tek_sayilar =0
#while sayac<=100:


    #if sayac % 2 ==0:
        #cift_sayilar += 1 

    #else:
        #tek_sayilar +=1

    #sayac +=1   #  sayac = sayac+1

#print(f'çift sayı: {cift_sayilar} \nTek sayı: {tek_sayilar}')

#ÖRNEK
#0 ile 100 arasındaki tüm pozitif tam sayıları toplayalım ve ekrana yazdıralım 

#sayac = 0
#toplam = 0
#while sayac <=100:

    #toplam += sayac
    #sayac += 1

#print(f'Toplam: {toplam}')


#ÖRNEK
#100 ile 0 arasındaki tüm çift ve tek sayıların ayrı ayrı toplamlarını bulalım


#sayac=100
#ciflerin_toplami = 0
#teklerin_toplami = 0
#while sayac >= 0:

  

    #if sayac % 2 == 0:
        #ciflerin_toplami += sayac

    #else:
        #teklerin_toplami += sayac
    #sayac -=1   #  sayac = sayac+1

   
#print(f'çift sayılatın toplamı: {ciflerin_toplami} \nTeklerin toplamı: {teklerin_toplami}')

#region soru-4
#? sonsuz döngü nasıl kurarım (WHİLE İLE)
#* Kullanıcıdan yapmak istediği işlem türünü alalım örneğin '+' , '-' etc.
#*2 tane tam sayı alalım. bir adım önce girdiği işlem türüne göre ilgili işlemi yapalım
#*işlem türü 'e' girene kadar işlem yapabilsin
#* kullanıcı 'e' işem türü girerse döngüyü nasıl durdururum?


#*sonsuz döngü
#while True:

#*kullanıcıdan işlem işte 

    #islem = input('islem_turu: ')

    #if islem == 'e':
        #print('Uygulama kapatılıyor..!')
       # break #?break deyimi döngüyü durdurur

    #elif islem == '+':
        #sayi_1= float (input ('Tam sayı giriniz:'))
        #sayi_2= float (input ('Tam sayı giriniz:'))

        #print (f'sonuç: {sayi_1+sayi_2}')
    #elif islem == '-':
        #sayi_1= float (input ('Tam sayı giriniz:'))
        #sayi_2= float (input ('Tam sayı giriniz:'))

       # print (f'sonuç: {sayi_1-sayi_2}')

    #elif islem == '*':
       # sayi_1= float (input ('Tam sayı giriniz:'))
        #sayi_2= float (input ('Tam sayı giriniz:'))

       # print (f'sonuç: {sayi_1*sayi_2}')

    #elif islem == '/':       

        #sayi_1= float (input ('Tam sayı giriniz:'))
       # sayi_2= float (input ('Tam sayı giriniz:'))

        #print (f'sonuç: {sayi_1/sayi_2}')
    #else :
        #print('Hatalı işlem türü..!')

#* ödevvvvvvv    her bir işlem türü için input almamak için nereye koymamız lazım

#? ÖDEV CEVAP: Eğer her bir işlem türü için tekrar tekrar input almak istemiyorsan,

# farklı işlemler yapılmasını istiyorsan, sayi_1 ve sayi_2 girişlerini while döngüsünün başına koy
#*cevap: 
#*YANLIŞ(DOĞRUSUNU BUL)
# Sonsuz döngü

# while True:
#     islem = input('İşlem türü seçin (+, -, *, /) veya çıkmak için e yazın: ')
#     if islem == 'e':
#         print('Uygulama kapatılıyor..!')
#         break
#     sayi_1 = float(input('1. sayıyı giriniz: '))
#     sayi_2 = float(input('2. sayıyı giriniz: '))
#     if islem == '+':
#         print(f'Sonuç: {sayi_1 + sayi_2}')
#     elif islem == '-':
#         print(f'Sonuç: {sayi_1 - sayi_2}')
#     elif islem == '*':
#         print(f'Sonuç: {sayi_1 * sayi_2}')
#     elif islem == '/':
#         if sayi_2 != 0:
#             print(f'Sonuç: {sayi_1 / sayi_2}')
#         else:
#             print("Hata: Sıfıra bölme yapılamaz!")
#     else:
#         print('Hatalı işlem türü..!')





#region soru-5

#?kullanıcı 3y gibi bir hata girerse diye hata ayıklıyotuz 

#while True:

    #try:
   
        #islem = input('islem_turu: ')

        #if islem == 'e':
                #print('Uygulama kapatılıyor..!')
                #break #?break deyimi döngüyü durdurur

        #elif islem == '+':
                #sayi_1= float (input ('Tam sayı giriniz:'))
                #sayi_2= float (input ('Tam sayı giriniz:'))

                #print (f'sonuç: {sayi_1+sayi_2}')
        #elif islem == '-':
                #sayi_1= float (input ('Tam sayı giriniz:'))
                #sayi_2= float (input ('Tam sayı giriniz:'))

                #print (f'sonuç: {sayi_1-sayi_2}')

        #elif islem == '*':
                #sayi_1= float (input ('Tam sayı giriniz:'))
                #sayi_2= float (input ('Tam sayı giriniz:'))

                #print (f'sonuç: {sayi_1*sayi_2}')

        #elif islem == '/':       

                #sayi_1= float (input ('Tam sayı giriniz:'))
                #sayi_2= float (input ('Tam sayı giriniz:'))

                #print (f'sonuç: {sayi_1/sayi_2}')
        #else :
                #print('Hatalı işlem türü..!')

    #except ValueError as err:
          #print(err)            



#region soru - 6 

#####* örnekkkk  kullanıcıdan alınan sayı asal mı değil mi test edelim


# sayi = int (input ('Bir sayı giriniz: '))

# if sayi <= 0:
#     print(f'{sayi} asal değildir')

# else:
#     is_prime = True 

#     if sayi == 1:

#      is_prime = False 

#     sayac = 2
#     while sayac < sayi :
#         if sayi % sayac == 0:
#             is_prime =  False
#             break    
#         sayac += 1 

#     if is_prime: #îs_prime== True : yada is_prime is true     
#        print(f'{sayi} asal değildir..!') 
#     else:
#         print(f'{sayi}asal değildir..!')      


# region soru- 7

#*kullanıcıdan alınan sayının faktöriyelini hesaplayalım.

# Kullanıcıdan sayı al
# sayi = int(input('Faktöriyeli alınacak sayıyı girin: '))

# if sayi < 0: # Negatif sayılar için kontrol
#     print('Negatif sayıların faktöriyeli tanımsızdır..!')
# else:
#     faktoriyel = 1
#     sayac = 1
#     while sayac <= sayi:
#         faktoriyel *= sayac
#         sayac += 1
#     print(f"{sayi}! = {faktoriyel}")
  
#* yada 

# sayi = int(input('Faktöriyeli alınacak sayıyı girin: '))
# if sayi < 0: # Negatif sayılar için kontrol
#     print('Negatif sayıların faktöriyeli tanımsızdır..!')

# elif sayi == 0 or sayi == 1:               
#     print('faktöriyel 1 dir...')
# else:
#     sonuc = 1 

#     while sayi > 0:
#         sonuc *= sayi
#         sayi -= 1
#         print(f'sonuç: {sonuc}')        



#! List
#! Birbirinden farklı değerlei içerisinde depolayan bir yapdıdır.
#? Index mekanizması vardır. Yani listenin ilk elemanı 0. indexte tutulur. Index pozitif yönde vektorel olara artan miktarda oluşr.

# #* Aşağıda bir liste örneği bulunmaktadır.
# boxers = ['mike tyson', 'muhammed ali', 'lenox lewis', 'evander holyfield', 'george foreman']

# #todo bir listenin elemanına onun index bilgisineden erişebiliriz
# print(boxers[0]) # output: 'mike tyson'
# print(boxers[4]) # output: 'george foreman'

# #! Listeler RAM'de saklanırlar bu yüzden uygulama kapatıldığında liste üzerinde yapılan işlemle silinir. 

# #? For loop ile bir liste içerisinde item item dolaşabiliriz
# for boxer in boxers:
#     print(boxer)

# #? boxers listesinin sonuna 'antony jasua' bilgisini ekleyelim
# boxers.append('antony jasua')
# print(boxers)

# #? boxers listesinin 4. indexsine 'deantony wilder' bilgisini ekleyelim
# boxers.insert(4, 'deantony wilder')
# print(boxers)


# #? 'antony jasua' bilgisni listeden silelim. 
# boxers.remove('antony jasua')

# #? 4. indexte tutulan bilgiyi silelim
# boxers.pop(4)

# current_boxers = ['antony jasua', 'tyson fury', 'deantony wilder']
# boxers.extend(current_boxers)

#* aşağıda random kütüpanesi içerisinde bulunana randint fonksiyonunu çalışma sayfamıza ekledik
#? randing fonksiyonu rastgele sayı üretmeye yarar.
# from random import randint

# sayilar = []  # boş bir liste yarattık

# for i in range(11):
#     rastegele_sayi = randint(0, 100)
#     sayilar.append(rastegele_sayi)

# print(sayilar)

#* Kullanıcıdan biz söz öbeği alalım. örneğin 'merhaba ben burak yılmaz'
#* kullanıcııdan alınan bu söz öbeğindeki tüm harfler küçük harfe dönüştürülsün.
#* ilgili söz öbeğindeki sesli harfler, sesli_harfler listesine
#* sessiz harfler ise, sessiz_harfler listesine eklensin
#* şayet kullanıcının girdiği ifade içerisinde rakam varsa bu karakter elensin
#* sesli_harfler ve sessiz_harfler listelerine bir harf sadece bir kere eklensin
#* söz öbeği içerisinde bir karakter varsa onuda elensin, örneğin burak1 yılmaz?

# word = input('Please type something: ').lower()

# butun_sesli_harfler = 'aeıioöuü'

# sesli_harfler = []

# sessiz_harfler = []

# for c in word:
#     #todo python içerisinde built-in olarka bulunan bu fonksiyon ilgili harfin a-z yada A-Z aralıüında olup olmadığını kontorol eder. şayet ilgili aralıkta ise True döner değilse False döner
#     if c.isalpha():
#         if c not in sesli_harfler and c not in sessiz_harfler:
#             if c in butun_sesli_harfler:
#                 sesli_harfler.append(c)
#             else:
#                 sessiz_harfler.append(c)

# print(f'Sesli Harfler: {sesli_harfler}\nSessiz Harfler: {sessiz_harfler}')

#* rastgele 10 tane sayı üretelim. 0 ile 100 arasında üretilen bu sayıları lst_1 listesinin içerisine dolduruyoruz
#* yukarı işlemi lst_2 listesi için yapıyor.
#* lst_1 ve lst_2'nin indexlerinde karşılıkle gelen değerleri toplayarak gene lst_3 ilgili indexsine yazıyoruz.
#* tüm soruyu index mantığı kullanarak çözüyoruz. 

# from random import randint

# lst_1 = []
# lst_2 = []
# lst_3 = []

# for i in range(10):
#     lst_1.insert(i, randint(0, 100))
#     lst_2.insert(i, randint(0, 100))

#     lst_3.insert(i, (lst_1[i] + lst_2[i]))

# print(f'1. liste: {lst_1}\n2. liste: {lst_2}\n3. liste: {lst_3}')



# users = ['hakan yıl_maz', '', '   ipek', 'burak yilmaz', 'kerim can atlıhan', 'elif rana esra altıntaş', 'munzur']
# # yukarı gele listedeki kullanıcılara kurumsal mail addresi yaratıyoruz.
# # input --> burak yılmaz
# # output --> burak.yilmaz@bilgeadam.com
# mail_addresses = []

# for user in users:

#     user_names = user.split(' ')

#     is_item_condition = []

#     for item in user_names:
#         if item.isalpha():
#            is_item_condition.append(True)
#         else:
#             is_item_condition.append(False)

#     if not any(i is False for i in is_item_condition):

#         if len(user_names) > 1:

#             mail_address = f'{user_names[0]}.{user_names[-1]}@bilgeadam.com'

#             mail_addresses.append(mail_address)

# print(mail_addresses)

# #! Nested List
# semtler = [
#     ['Sarıyer', 'Beşiktaş', 'Ulus'],
#     ['Suadiye', 'Feneryolu'],
#     ['Bebek', ['Hacıhüsrev', 'Tarlabaşı']],
#     ['Ataköy', 'Bakırköy', 'Yeşilköy']
# ]

# print(semtler[0]) #? ['Sarıyer', 'Beşiktaş', 'Ulus']
# print(semtler[0][2]) #? 'Ulus'
# print(semtler[2][1][0]) #? 'Hacıhüsrev'

# #! Unboxing

# my_family = [
#     ['Burak Yılmaz', 'beast', 36],
#     ['Hakan Yılmaz', 'savage', 39],
#     ['ipek Yılmaz', 'keko', 41],
# ]

# for full_name, user_name, age in my_family:
#     print(f'Full Name: {full_name}\nUser Name: {user_name}\nAge: {age}')


# from hashlib import sha256

# # aşağıdaki listede bulunan kullanıcıların şifrelerini hash'leyerek aynı kullanıcının listesine ekleyin
# users = [
#     ['beast', '123'], 
#     ['savage', '987'],
#     ['bear', '578']
# ]

# counter = 0
# for username, password in users:
#     hash_object = sha256(password.encode())
#     hashed_password = hash_object.hexdigest()
#     users[counter].remove(password)
#     users[counter].append(hashed_password)
#     counter += 1

# print(users)


# List Coprehansion
# lst = [i for i in range(10)]
# print(lst)

# # rakamların karelerini barındıran listeyi hazırlayın
# print([i * i for i in range(10)])

# # 0 ile 100 arasında 3 tam bölünen sayıları içeren listeyi hazırlayın
# print([i ** 3 for i in range(100) if i % 3 == 0])


#* for i in range(1, 11):
#*     for j in range(1, 11):
#*         print(f'{i} x {j} = {i * j}')
#*     print('============')

# print([[f'{i} x {j} = {i * j}' for j in range(1, 11)] for i in range(1, 11)])


# from random import randint

# print([randint(0, 100) for i in range(10)])

# any(): bir liste içerisinde tüm değerler küçük harfi, digit mi?, liste içerisinde username 'beast' olan var mı? liste içerisinde ki değerler alfabetik mi?
# from string import punctuation

# full_name = 'burak _yılmaz'
# if any(harf in punctuation for harf in full_name):
#     print('İsim noktalama işareti içerisyor..!')
# else:
#     print('İçemiyor..!')

# katilimcilar = ['Baran', 'Emre', 'Elif', 'Munzur']
# isim = input('Aradığınız katılımcı adını giriniz: ')
# if any(isim == kalitimci for kalitimci in katilimcilar):
#     print('Aradığınız katılımcı burada')
# else:
#     print('Katılmamıştır..!')

# password = 'burak1'

# if any(harf.isdigit() for harf in password):
#     print('rakam içeririr')
# else:
#     print('rakam içermez')

# if not any(harf.isdigit() for harf in password):
#     print('rakam içermez')
# else:
#     print('rakam içeririr')

# all(): liste içerisinde ki tüm değerler aynı ise True değilse False dönder
# numbers: list[int] = [1, 2, 6, 4, 5]
# print(all(numbers))

# mixed_list = [1, 2, None, 4, 5]
# print(all(mixed_list))


# print(all([x > 0 for x in range(-5, 5)]))



# filter(): Bu fonksiyon vasıtasyıla bir liste içerisinden sadece istediğim değerleri çekiyorum yani listemi filtreliyorum
# values = [0, '', 1, 'Python', None, True, 3.14, False]
# result = filter(None, values)
# print(list(result))


# numbers = [-2, -10, 0 , 5, 6]
# positives = filter(lambda x: x > 0, numbers)
# print(list(positives))

# aşağıdaki listende çift sayıları fitreleyin
# numbers = [1, 2, 3, 4, 6]
# evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))


# meyveler = ['elma', 'armut', 'karpuz', 'çilek', 'muz']
# # karpuz bilgisini fitreleyin
# meyve = list(filter(lambda x: x == 'karpuz', meyveler))
# print(meyve)

# users = ['savage', 'beast', 'bear']
# # içinde z geçmeyen kullanıcıları filtreleyin
# contains_z = list(filter(lambda x: 'z' in x, users))
# not_contains_z = list(filter(lambda x: 'z' not in x, users))


# map(): verilerin tiplerini değiştirir.
years = [i for i in range(1923, 2026)]

print(years)

str_years = list(map(str, years))
print(str_years)

# enumarate(): bir listenin index ve o index'te tutulan değerini verir.
for index, value in enumerate(years):
    print(f'Incex: {index} - Value: {value}')

# Walrus Operatör
# aynı anda hem if kontrolü hemde değer ataması yapılabilinir. List Comprehsion yoğun olarak tercih edilir.
if (n := len('merhaba')) > 5:
    print(f'{n}')

sayilar = [1, 2, 3, 4, 5]

print([y for x in sayilar if (y := x * 2) > 6])

# password is valid?
# kullanıcıdan bir password alıyoruz
# ilgiil password en az 16 karakterli olmalı
# en az bir büyük harf içermlei, bir küçük harf içermeli
# en az bir noktalama işareti içermeli
# en az bir rakam içermeli
# burakBurak1?burak

from string import punctuation

conditions = []
users = [
    # ['username', 'password']
]

user_name = input('Please type your user name: ')
password = input('Please type your password: ')

if len(password) <= 16:
    conditions.append(False)
if not any(c.isupper() for c in password):
    conditions.append(False)
if not any(c.islower() for c in password):
    conditions.append(False)
if not any(c.isdigit() for c in password):
    conditions.append(False)
if not any(c in punctuation for c in password):
    conditions.append(False)

if not any(x is False for x in conditions):
    print('Your account has been created..!')
    users.append([user_name, password])
    print(users)
else:
    print('Invalid credentials..!')



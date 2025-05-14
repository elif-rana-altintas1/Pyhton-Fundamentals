#! Karar Mekanızması
#? Belirli bir şarta göre işlemlerin yapılmasını istiyorsak karar mekanizması kullanacağız. Python da iki tip karar mekanızması bulunmaktadır. birisi if-else diğeri ise match-case.

#* If-Else
# x = 5
# y = 6

# if x > y:
#     print(f'{x} büyüktür..!')
# else:
#     print(f'{y} büyüktür..!')

#! Kullanıcıdan alınan sayı çift mi tek mi ?
# x = int(input('Tam Sayı Giriniz: '))

# if x % 2 == 0:
#     print(f'{x} çift sayıdır..!')
# else:
#     print(f'{x} tek sayıdır..!')

#! Kullanıcıdan alınan sayı pozitif mi negatif mi nötr mü yazdırınız?
# number = int(input('Sayı giriniz: '))

# if number == 0:
#     print(f'{number} nötür..!')
# elif number > 0:
#     print(f'{number} pozitiftir..!')
# else:
#     print(f'{number} negatiftir..!')

#region Soru
#! Kullanıcıdan mevsim bilgisi alalım.
#! İlgili mevsim bilgisine göre ayları ekrana yazdıralım
#todo Not: python case sensetive yani büyük küçük harf duyarlıdır
# mevsim = input('Mevsim: ')

# if mevsim == 'kış':
#     print(f'Aralık-Ocak-Şubat')
# elif mevsim == 'ilkbahar':
#     print(f'Mart-Nisan-Mayıs')
# elif mevsim == 'yaz':
#     print(f'Haziran-Temmuz-Ağustos')
# elif mevsim == 'sonbahar':
#     print(f'Eylük-Ekim-Kasım')
# else:
#     print('Böyle bir mevsim yok uzaylı mısın?')

#? match-case
# mevsim = input('Mevsim: ')

# match mevsim:
#     case 'kış':
#         print(f'Aralık-Ocak-Şubat')
#     case 'ilkbahar':
#         print(f'Mart-Nisan-Mayıs')
#     case 'yaz':
#         print(f'Haziran-Temmuz-Ağustos')
#     case 'sonbahar':
#         print(f'Eylük-Ekim-Kasım')
#     case _:
#         print('Böyle bir mevsim yok uzaylı mısın?')

#region Soru
# Kullanıcıdan alınan 3 tane sayıdan buyük olanı ekrana yazdıralım
# a > b ve a > c
# b > a ve b > c
# c > a ve c > b
# a = int(input('Sayı: '))
# b = int(input('Sayı: '))
# c = int(input('Sayı: '))

# if a > b and a > c:
#     print(f'{a} en büyük sayıdır..!')
# elif b > a and b > c:
#     print(f'{b} en büyük sayıdır..!')
# elif c > a and c > b:
#     print(f'{c} en büyük sayıdır..!')
# else:
#     print('sayılar bir birine eşit olabilir...!')

#endregion

#region Soru
#* Kullanıcıdan aradığı ürün bilgisini alalım.
#* Ürün muz, domates, karpuz ise sebze reyonuna
#* kindle, tablet, notebook ise teknoloji retonuna
#* şampuan, sabun, parfüm ise kozmatik reyonuna yönlendiriniz
# product = input('Aradığınız ürünü girin: ')

# if product == 'muz' or product == 'karpuz' or product == 'kavun':
#     print('Aradığınız ürün, {product} sebze reyonundadır..!')
# elif product == 'kindle' or product == 'tablet' or product == 'notebook':
#     print('Aradığınız ürün, {product} teknoloji reyonundadır..!')
# elif product == 'şampuan' or product == 'sabun' or product == 'parfüm':
#     print('Aradığınız ürün, {product} kozmatik reyonundadır..!')
# else:
#     product('Aradığınız ürün bulunmamaktadır..!')
#endregion

#region Soru
#* username, beast
#? password, 123 ise hoşgeldiniz değilse hatılı kullanıcı bilgileri
#! NOT: burada lower() built-in yani gömülü olarak bulnan fonksiyon vasıtasıyla küçük harfe dönüştürebilir
# user_name = input('User Name: ').lower() 
# password = input('Password: ')

# if user_name == 'beast' and password == '123':
#     print('Hoşgeldiniz, {user_name}')
# else:
#     print('Hatalı kullanıcı bilgileri..!')
#endregion

#region Soru
#* Kullanıcıdan satın adlığı kitap sayını alalım
# *bir kitap 5 TL
# *1-5 tane kitap alırsa yüzde 5 iskonto
# *6-10 tane alırsa yüzde 10
# *11-15 tane alırsa yüzde 15
# *16-20 tane alıtsa yüzde 20 
# *ödeyeceği nihai tutar ekrana yazılsın

# kitap_sayisi = int(input('Kitap Sayısı: '))
# if kitap_sayisi >= 1 and kitap_sayisi <= 5: # 1 <= kitap_sayisi <= 5:
#     print(f'Ödenecek Tutar: {kitap_sayisi * 5 * 0.95}…


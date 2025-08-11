

#! Custom Functions
#? Bu ana kadar python içerisinde built-in (yerleşik-gömülü) olarka bulunan fonksiyonlardan faydalandık. Bu fonksiyonlar spesifik işler işler çözen yapılardır. Artık kendi ihtiyaç duyduğumuz işlemleri çözleteceğimiz fonksiyonlar yazacağız.
#* Fonksiyon kullanamk temiz kod yazma için atılması gereken ilk adımdır. Bize merkezi bir yönetim sağlar. Yazdığımız fonksiyonları istediğimiz yerde istediğmiz kadar çağırabiliriz. 

#! fonksiyonumuz define ettik yani tanımladık
# def hello():
#     print('Hello Kerem')


# #! artık fonksiyonumuzu istediğimiz yerde istediğmiz kadar çağırabilirriz yani execute edebiliriz
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()


# #! fonksioynları dinamikleştirmek istersek
# #? bu işlemi argümanlar ile yaparız
# #* argümanlar dışarıdan gelen değerleri fonkisyonun içerisine taşırlar
# def greeting_people(first_name: str):
#     print(f'{first_name} hello..!')


# greeting_people(first_name='Burak')
# greeting_people(first_name='Elif')
# greeting_people(first_name='Kerem')


# #* 2 tane pozitif tam sayıyı toplayan ve soncuunu print eden fonksiyonu yazın
# def sum_two_number(number_1: int, number_2: int):
#     print(f'{number_1} + {number_2} = {number_1 + number_2}')

# sum_two_number(number_1=5, number_2=10)
# sum_two_number(number_1=3, number_2=40)
# sum_two_number(number_1=90, number_2=258)


# #* bir tam sayının tek mi çift mi olduğunu çıktı veren fonkisyonu yazın
# def even_or_odd(number: int):
#     if number % 2 == 0:
#         print(f'{number} is even..!')
#     else:
#         print(f'{number} is odd..!')

# even_or_odd(number=2)
# even_or_odd(number=11)
# even_or_odd(number=12)

# #! Değer döndüren fonkisoynlar
# #? Yaptığı işlem sonucunda bize bir değer döndüren fonksiyonlara denir. Örneğin split() fonkisyonu çalışmasını tamamladığında bizelere liste dönüyordu.

# def toplam(s1: int, s2: int, s3: int) -> int:
#     """This functions adds 3 numbers.

#     Args:
#         s1 (int): Type must be integer
#         s2 (int): Type must be integer
#         s3 (int): Type must be integer

#     Returns:
#         int: This function return integer type value
#     """
#     return s1 + s2 + s3


# result = toplam(s1=12, s2=4, s3=9)
# print(result)

# #! bir listede ki sayıların geçme sıklığını yani frekans aralığını bulan fonksiyonu yazlaım
# rakamlar = [1, 1, 1, 5, 4, 5, 2, 2, 1, 5, 4, 3, 3]

# def frequency_count(numbers: list) -> dict:
#     frequency_dict = {}

#     for item in numbers:
#         if item in frequency_dict:
#             frequency_dict[item] += 1
#         else:
#             frequency_dict[item] = 1
    
#     return frequency_dict


# print(frequency_count(numbers=rakamlar))


# #* Bir söz öbeğinde tekrar eden kelimelerden arındırak çıktı veriniz
# #? örnek input --> merhaba ben burak burak ben merhaba
# #! örnek output --> merhaba ben burak

# def remove_dublicate_word(sentence: str) -> str:
#     temp_list = []

#     for item in sentence.split(' '):
#         if item not in temp_list:
#             temp_list.append(item)
    
#     return ' '.join(temp_list)

# print(remove_dublicate_word(sentence='merhaba ben burak burak ben merhaba'))


# #! kullanıcıdan firstname ve lastname ayrı ayrı alan ve kurumsal mail adresi oluşturan fonksiyonu yazın.
# def create_mail_adress(firstname: str, lastname: str) -> str:
#     return f'{firstname}.{lastname}@bilgeadam.com'

# print(
#     create_mail_adress(
#         firstname=input('First Name: '),
#         lastname=input('Last Name: ')))

#! password argüman olarak fonksiyona iletilecek hashlenmiş hali return edilecek
# from hashlib import sha256

# users = {
#     1: {
#         'username': 'beast',
#         'password': '123'
#     },
#     2: {
#         'username': 'savage',
#         'password': '987'
#     }
# }

# def get_password(data: dict) -> str:
#     temp_list = []

#     for user in data.values():
#         temp_list.append(user.get('password'))

#     return temp_list


# def hash_password(password: str) -> str:
#     hash_object = sha256(password.encode())
#     hash_password = hash_object.hexdigest()
#     return hash_password

# for pwd in get_password(data=users):
#     print(hash_password(password=pwd))


#! faktoriyel hesaplayan bir fonksiyon yazalım
# def calculate_factorial(number: int) -> int | str:
#     if number < 0:
#         return 'Negatif sayıların faktöriyeli hesaplanamaz..!'
#     elif number == 0 or number == 1:
#         return 'Faktöriyel 1..!'
#     else:
#         sonuc = 1

#         while number > 0:
#             sonuc *= number
#             number -= 1
        
#         return sonuc


# print(f'Sonuç: {calculate_factorial(number=5)}')


# rastgele 10 tane sayı üretelim. üretilen bu sayıları bir liste içerisine dolduralım
# from random import randint

# def create_random_numbers(amount: int, start_point: int, end_point: int) -> list:
#     return [randint(start_point, end_point)  for i in range(amount)]

# print(create_random_numbers())
from pprint import pprint

products = [
    {
        "ProductID": 1,
        "ProductName": "Chai",
        "SupplierID": 1,
        "CategoryID": 1,
        "QuantityPerUnit": "10 boxes x 20 bags",
        "UnitPrice": 18.0,
        "UnitsInStock": 39,
        "UnitsOnOrder": 0,
        "ReorderLevel": 10,
        "Discontinued": False
    },
    {
        "ProductID": 2,
        "ProductName": "Chang Syrup",
        "SupplierID": 1,
        "CategoryID": 1,
        "QuantityPerUnit": "24 - 12 oz bottles",
        "UnitPrice": 19.0,
        "UnitsInStock": 17,
        "UnitsOnOrder": 40,
        "ReorderLevel": 25,
        "Discontinued": False
    },
    {
        "ProductID": 3,
        "ProductName": "Aniseed Syrup",
        "SupplierID": 1,
        "CategoryID": 2,
        "QuantityPerUnit": "12 - 550 ml bottles",
        "UnitPrice": 10.0,
        "UnitsInStock": 13,
        "UnitsOnOrder": 70,
        "ReorderLevel": 25,
        "Discontinued": False
    },
    {
        "ProductID": 4,
        "ProductName": "Chef Anton's Cajun Seasoning",
        "SupplierID": 2,
        "CategoryID": 2,
        "QuantityPerUnit": "48 - 6 oz jars",
        "UnitPrice": 22.0,
        "UnitsInStock": 53,
        "UnitsOnOrder": 0,
        "ReorderLevel": 0,
        "Discontinued": False
    },
    {
        "ProductID": 5,
        "ProductName": "Chef Anton's Gumbo Mix",
        "SupplierID": 2,
        "CategoryID": 2,
        "QuantityPerUnit": "36 boxes",
        "UnitPrice": 21.35,
        "UnitsInStock": 0,
        "UnitsOnOrder": 0,
        "ReorderLevel": 0,
        "Discontinued": True
    }
]

def get_product_by_categoryid(data: list, category_id: int):
    for item in data:
        if item['CategoryID'] == category_id:
            return item
        
def get_product_by_name(data: list, product_name: str) -> str:
    for item in data:
        if item['ProductName'].__contains__(product_name):
            return f'Product Name: {item['ProductName']}\nUnit Price: {item['UnitPrice']}\nStock: {item['UnitsInStock']}'
    else:
        return 'Aradığınız ürün bulunmamaktadır..!'

pprint(get_product_by_categoryid(data=products, category_id=2))












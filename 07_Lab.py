
# #!Tuples (Demetler)
# #?listeler gibi demetlerde index mantığıyla çalışan değişik tiplerde veri tutan bir başka yapıdır Listelerin sahip olduğu gibi built-in fonksiyonlara sahip değildir
# #todo demetler içerisinde değiştirilmeyecek sabit veriler tutulur. Yani demetleri Read Only oku ve kullan amaçlı tercih edeceğiz.Bu bağlamda listelerden daha hızlı çalışırlar.

# #*Create-update-delete gibi operasyonlar yapamayız

# # tuple_1=('Galatasaray','Beşiktaş','Trabzonspor','Adanademir Spor','Fenerbahçe')
# # tuple_2=('12','35.5','Eagels','Red Skins','Seahawks','Patriots')
# # tuple_3=tuple_1+tuple_2
# # print(tuple_3)

# #!Dilimleme(Slicing)
# #?Hem demetlerde hem de listelerde kullanılan bir mantıktır.
# # print(tuple_3[0:5])
# # print(tuple_3[1:3])
# # print(tuple_3[::2])  # 2-2 zıplayarak gider
# # print(tuple_3[1::3])
# # print(tuple_3[::-1])# listeyi tersten yazdırır
# # print(tuple_3[::-3])
# # print(tuple_3[4::-2])



# #! Dictionary (Sözlük)
# #?Sözlükler,List ve tuple gibi bir başka yapımızdır.Pyhton'da yoğun olarak kullanılırlar. Anahtar & değer mantığıyla çalşırlar.
# # my_dict={
# #     'Full Name':'Burak Yılmaz',
# #     'Age':36,
# #     'İnterested sports':['Boxing','Wrestling','UFC'],
# #     'Favorite Books':{
# #         'War History':('cambridge war history','battle of waterloo'),
# #         'scientific':{
# #             'Karl Poper':'The Logic of Scientific discovery'
# #         }
# #     }
# # }
# #*ÖRNEK
# # movies={
# #     'Fight Club':1999,
# #     'The Matrix':1999,
# #     'Interstaller':2014,
# #     'Inception':2010,
# #     'Dune':2021,
# # }

# #*Fight club anahtarına ait value ekrana yazdıralım.

# #Path-1
# #print(movies['Fight Club'])

# #Path-2
# #print(movies.get('Fight Club'))      

# #*sözlüğün tüm anahtarlarını ekrana yazdıralım (for loopla)

# # for movie in movies:
# #     print(movie)
# #*sözlüğün tüm valuelarını ekrana yazdıralım (for loopla)

# # for value in movies.values() :
# #     print(value)

# # for key , value in movies.items():
# #     print(f'{key}-{value}')
# #?CRUD (Create-read-update-delete)

# # #TODO CREATE
# # movies['Tennet']=2022

# # #TODO UPDATE
# # movies
# #! Tuples (Demetler)
# #? Listeler gibi demetlerlde index mantığla çalışan, değişik tiplerde veri tutan bir başka yapdırı. Listlerin sahip olduğu gibi built-in fonksiyonlara sahip değildir.
# #todo Demetler içerisinde değiştirilemeyecek sabit veriler tutulur. Yani demetleri Read Only sadece oku ve kullan amaçlı tercih edeceğiz. Bu bağlamda listelerden daha hızlı çalışırlar. 
# #* Create-Update-Delete gibi operasyonları yapamayız.

# # tuple_1 = ('Galatasaray', 'Beşiktaş', 'Trabzonspor', 'Adanademir Spor', 'Fenerbahçe')
# # tuple_2 = ('12', '35.5', 'Eagels', 'Red Skins', 'Seahawks', 'Patriots')

# # tuple_3 = tuple_1 + tuple_2 #* liste ve tuple burada olduğu gibi birleştirebiliyoruz

# # print(tuple_3)

# # #! Dilimleme (Slicing)
# # #? Hem demetlerde hemde listelerde kullanılan bir mantıktır.
# # print(tuple_3[0:5])
# # print(tuple_3[1:3])
# # print(tuple_3[::2])
# # print(tuple_3[1::3])
# # print(tuple_3[::-1])
# # print(tuple_3[::-2])
# # print(tuple_3[4::-2])

# #! Dictionary (Sözlük)
# #? Sözlükler, list ve tuple gibi bir başka yapımızdır. Python'da yoğun olarka kullanılırlar. Anahtar & değer mantığında çalışırlar. 

# # my_dict = {
# #     'Full Name': 'Burak Yılmaz',
# #     'Age': 36,
# #     'Interested Sports': ['Boxing', 'Wrestling', 'UFC'],
# #     'Favorite Books': {
# #         'War History': ('Cambridge War History', 'Battle of Waterloo'),
# #         'Scientific': {
# #             'Karl Poper': 'The Logic of Scienrtific Discovery'
# #         }
# #     }
# # }


# # movies = {
# #     'Fight Club': 1999,
# #     'The Matrix': 1999,
# #     'Interstaller': 2014,
# #     'Inception': 2010,
# #     'Dune': 2021
# # }

# # #! Fight Club anahtarına ait value ekrana yazdıralım
# # #* Path I
# # print(movies.get('Fight Club'))
# # #* Path II
# # print(movies['Fight Club'])

# # #* Sözlüğün tüm anahtarlarnı ekrana yazdırın
# # for key in movies.keys():
# #     print(key)

# # #* Sözlüğün tüm value ekrana yazdırın
# # for value in movies.values():
# #     print(value)

# # for key, value in movies.items():
# #     print(f'{key} - {value}')

# # #? CRUD (CREATE-READ-UPDATE-DELETE)
# # #todo Create
# # movies['Tennet'] = 2022

# # #todo Update
# # movies.update({
# #     'Tennet': 2021
# # })

# # #todo Delete
# # del movies['Tennet']


# from uuid import uuid4
# from pprint import pprint

# # print(uuid4())
# # print(uuid4()) #? c8eb49c4-bfae-4bf4-bb36-2fec995362f2

# categories = {
#     '6df9bada': {
#         'category name': 'Boxing Gloves',
#         'description': 'Best boxing gloves'
#     },
#     '6a9333de': {
#         'category name': 'Punching Bags',
#         'description': 'Best punching bags'
#     }
# }

# while True:
#     process = input('Please choose a process menu: ')

#     match process:
#         case 'create':
#             _id = str(uuid4()).split('-')[0]
#             categories[_id] = {
#                 'categoy name': input('Category Name: '),
#                 'description': input('Description: ')
#             }
#             print(f'{_id} has been created..!')
#             pprint(categories)
#         case 'list':
#             pprint(categories)
#         case 'update':
#             _id = input('Id: ')
#             new_category_name = input('Category Name: ')
#             new_description = input('Description: ')

#             categories.update({
#                 _id: {
#                     'category name': new_category_name,
#                     'description': new_description
#                 }
#             })

#             print(f'{_id} has been editid..!')
#             pprint(categories)
#         case 'delete':
#             _id = input('Id: ')

#             del categories[_id]

#             print(f'{_id} has been removed..!')
#             pprint(categories)
#         case 'exit':
#             print('Application has been closing..!')
#             break #? break deyimi gibi birde contiune deyimi bulunmaktadır. break ile continue altında kalan kodlar çalışmaz.
#         case _:
#             print('Please choose a valid process..!').update({
# #     'Tennet':2021

# # })    

# # #TODO DELETE
# # del movies['Tennet']




# #*******ÖRNEK

# # from uuid import uuid4
# # from pprint import pprint
# # # print(uuid4())
# # # print(uuid4())



# # categories={
# #     '3bae3182':{
# #         'category name':'boxing gloves',
# #         'description':'best boxing gloves'
# #     },
# #     '4a76c95e':{
# #         'category name':'punching bags',
# #         'description':'best punching bags'
# #     }

# # }


# # while True:
# #     process=input('please choose a process menu:')

# #     match process:
# #         case 'create':
# #             _id=str(uuid4()).split('-')[0]
# #             categories[_id]={
# #                 'category name':input('category name:'),
# #                 'description':input('description')
# #             }
# #             print(f'{_id} has been created..!')
# #             pprint(categories)
                
# #         case 'list':
            
# #             pprint(categories)
            
# #         case 'update':
           
       
# #             _id = input('Enter the category ID to update: ')
# #             new_category_name=input('category name :')
# #             new_description=input('description')
# #             categories.update({
# #                  _id:{
# #                       'category name':new_category_name,
# #                       'description':new_description
# #                  }
# #             })
           

# #             print(f'{_id}has been editid..!')
# #             pprint(categories)

# #         case 'delete':
# #             _id = input('Enter the category ID to update: ')
# #             del categories[_id]
# #             print(f'{_id}has been removed..!')
# #             pprint(categories)
# #         case 'exit':
# #             print('application has been closing..!')
# #             break #?break deyimi gibi birde continue deyimi bulunmaktadır. break ile continue altında kalan kodlar çalışmaz
# #         case _:
# #             print('please choose a valid process..!')


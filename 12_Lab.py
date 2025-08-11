
#! File I/O
#? Dosya açma, kapama ve üzerinde çalışma işlemlerini gerçekleştirmek için kullanılan bir kütüphanedir.

# # region Dosya Açma
# file = open(
#     file='new_file.txt',
#     mode='w',
#     encoding='utf-8'
# )
# file.write('Full Name: Burak Yılmaz\nOccupation: Developer\n')
# file.close()
# # endregion


# # region Updata file
# file = open(
#     file='new_file.txt',
#     mode='a',
#     encoding='utf-8'
# )
# file.write('Programing Language: Python\n')
# file.close()
# # endregion

# # region Read File
# file = open(
#     file='new_file.txt',
#     mode='r',
#     encoding='utf-8'
# )
# for line in file.readlines():
#     print(line)
# # endregion


# region Task 1
def create_exam_grades() -> None:
    """_summary_: Create a file which it will be use exam grades
    """
    file = open(
        file='exam_grades.txt',
        mode='w',
        encoding='utf-8'
    )
    file.close()
# endregion

# region Task 2
# Kullanıcıdan bize first name, last name, midterm, final, homework  bilgileri geliecek.
# bu gelen bilgileri aşağıdaki formatta, exam_grades dosyasına ekleyelim
# Burak Yılmaz:30,30,30
# ilgili dosya ile çalışırken "with open()" fonksiyonunu kullanalım
def take_grades(first_name: str, last_name: str, midterm: float, final: float, homework: float):
    with open(file='exam_grades.txt',mode='a',encoding='utf-8') as file:
        file.write(f'{first_name} {last_name}:{midterm},{final},{homework}\n')
# endregion

# region Task 3
# Harf Notunu hesaplayan bir fonksiyon yazın
# Fonksiyona gelen bir satır bilgi aşağıdaki gibir
# Burak Yılmaz:30,30,30
# Harf notunu hesapla ve return et
# Sample Return --> Full Name: FF
def calculate_letter_grade():
    pass
# endregion
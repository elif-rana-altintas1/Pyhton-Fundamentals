
from socket import gethostname, gethostbyname
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#? Bir fonksiyon her kullanıldığında farklı miktarlarda yani sabit olmayacak şekilde argüman alıyorsa bu senaryoda *args, **kwargs
#! *args --> girilen argümanları fonksiyona tuple olarak taşır
#! **kwargs --> argümanları dictionary olarak fonksiyona taşır

def log_critograph(**kwargs):
    
    try:
        personal_id = int(input("id:  "))
        print(f"personal id:{personal_id}")

    except ValueError as err:
        aes_key = get_random_bytes(16)
        aes_obj = AES.new(key=aes_key, mode=AES.MODE_CBC, iv=get_random_bytes(16))
        padded_data = b"valueerrorhappen" + b" " * (16 - len(b"valueerrorhappen") % 16)
        chipper_text = aes_obj.encrypt(padded_data)

        with open(file=kwargs.get("file_name"), mode="a", encoding="utf-8") as log_file:
            log_file.write(str(chipper_text))
            log_file.write('\n')
            log_file.write(f'Machien Name: {kwargs.get("machine_name")}')
            log_file.write('\n')
            log_file.write(f'IP Address: {kwargs.get("ip_address")}')
            log_file.write('\n')
            log_file.write(f'Exception Time: {kwargs.get("exception_date")}')
            print(f'Personal id has not any characher..\n(err)')

    
log_critograph(
    file_name="log.txt",
    machine_name=gethostname(),
    ip_address=gethostbyname(gethostname()),
    exception_date=datetime.now()
)







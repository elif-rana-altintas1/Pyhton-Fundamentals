
# region data
burak_account = {
    'account no': '12345',
    'full name': 'Burak Yılmaz',
    'password': '123',
    'balance': 3000,
    'additional balance':1000
}

hakan_account = {
    'account no': '98765',
    'full name': 'Hakan Yılmaz',
    'password': '123',
    'balance': 4000,
    'additional balance':1000
}

ipek_account = {
    'account no': '45678',
    'full name': 'İpek Yılmaz',
    'password': '123',
    'balance': 6000,
    'additional balance':1000
}

users = [burak_account, hakan_account, ipek_account]
# endregion

# region Balance Result
def balance_result(account: dict) -> str:
    return (
        f'Account No: {account["account no"]}\n'
        f'Balance: {account["balance"]}\n'
        f'Additional Balance: {account["additional balance"]}'
    )
# endregion

# region Withdrow Money
#? Para Çekme Business Logic
#* 1. account'un balance'sı amount karşılarsa
#* 2. amount balance'tan büyükse kullanıcıya additional balance kullanılınsın mı? soralım
#* yes derse balance + additinal balance amount büyükse eşitse işlem gerçekleşsin değilse iptal olsun
def witdrow_money(amount: int, account: dict) -> None:
    if account['balance'] >= amount:
        account['balance'] -= amount
        print(balance_result(account=account))
    else:
        total_balance = account['balance'] + account['additional balance']

        if total_balance >= amount:
            use_additional_balance = input('Insufficent balance. Do you want to use additional balance?')

            match use_additional_balance:
                case 'y':
                    account['balance'] = 0
                    account['additional balance'] = total_balance - amount
                    print(balance_result(account=account))
                case 'n':
                    print('Transaction has been cancaled..!')
                    print(balance_result(account=account))
                case _:
                    print('Please choose valid answer.(yes or no)..!')

        else:
            print('Insufficen total balance. Transaction has been cancaled..!')
            print(balance_result(account=account))
# endregion

# region Deposit Money
def deposit_money(account: dict, amount: int, transaction_type: str) -> None:
    account['balance'] += amount
    if account['additional balance'] < 1000:
        transfer_amount = 1000 - account['additional balance']
        account['balance'] -= transfer_amount
        account['additional balance'] += transfer_amount
    
    if transaction_type != 'eft':
        print(balance_result(account=account))
# endregion

# region EFT
def eft_transaction(sender_account: dict, receiver_account_no: str, amount: int) -> None:
    for user in users:
        if user['account no'] == receiver_account_no:
            witdrow_money(account=sender_account, amount=amount)
            deposit_money(account=user, amount=amount, transaction_type='eft')

# endregion

# region Login
def login(account_no: str, password: str) -> dict | None:
    for user in users:
        if user['account no'] == account_no and user['password'] == password:
            return user
    
    return None
# endregion

def main():
    user_account = login(
        account_no=input('Account No: '),
        password=input('Password: ')
    )

    if type(user_account) is dict:
        while True:
            process = input('Please choose a process: ')
            match process:
                case '1':
                    withdrow_amount = int(input('Amount: '))
                    witdrow_money(
                        account=user_account,
                        amount=withdrow_amount
                    )
                case '2':
                    deposit_amount = int(input('Amount: '))
                    deposit_money(
                        account=user_account,
                        amount=deposit_amount,
                        transaction_type=''
                    )
                case '3':
                    eft_amount = int(input('Eft Amount: '))
                    revirver_no = input('Receiver No: ')
                    eft_transaction(
                        sender_account=user_account,
                        receiver_account_no=revirver_no,
                        amount=eft_amount
                    )
                case 'e':
                    print('Application has been closing..!')
                    break
                case _:
                    print('Please type a valid process number..!')
    else:
        print('Invlaid credentials..!')

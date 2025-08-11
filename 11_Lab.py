

#! Basit bir barbut oyunu

from random import randint, choice

bots = ['munzur karabulut', 'elif altıntaş', 'kerem atlıhan']

minimum_bet = 100

user_dict = {
    '1': {
        'user name': 'beast',
        'password': '123',
        'safe': 2000
    },
    '2': {
        'user name': 'savage',
        'password': '987',
        'safe': 3000
    }
}

def assing_default_player(custom_list: list) -> str: 
    return choice(custom_list)

def roll_dice() -> int:
    return randint(2, 12)

def gain_daily_chips() -> int:
    return randint(1000, 2000)

def is_bet_valid(current_bet: int, safe: int) -> bool:
    if minimum_bet <= current_bet <= safe:
        return True
    else:
        return False

def update_safe(user: dict, chip_amount: int, winning_status: bool) -> str:
    if winning_status: # status is True
        user.update({
            'safe': user.get('safe') + chip_amount
        })
        return (
            f'Congratulations..!\n'
            f'Your current safe is {user.get("safe")}'
        )
    else:
        user.update({
            'safe': user.get('safe') - chip_amount
        })
        return (
            f'Loose..!\n'
            f'Your current safe is {user.get("safe")}'
        )

def login(user_name: str, password: str) -> dict | None:
    for i in range(1, len(user_dict) + 1):
        if user_dict.get(str(i)).get('user name') == user_name and user_dict.get(str(i)).get('password') == password:
            return user_dict.get(str(i))
    return None

def main():
    user = login(
        user_name=input('User Name: '),
        password=input('Password: ')
    )
    
    if user is not None:
        daily_chips = gain_daily_chips()
        
        print(update_safe(user=user, chip_amount=daily_chips, winning_status=True))
        
        while True:
            if user.get('safe') >= minimum_bet:
                if player_bot is None:
                    player_bot = assing_default_player(custom_list=bots)
                        
                    print(f'{player_bot} has been set to the table..!')
                
                bet = int(input('Please make a bet: '))
                
                if is_bet_valid(current_bet=bet, safe=user.get("safe")):
                    player_1_roll = roll_dice()
                    player_2_roll = roll_dice()
                    
                    if player_1_roll > player_2_roll:
                        print(update_safe(user=user, chip_amount=bet, winning_status=True))
                    elif player_1_roll < player_2_roll:
                        print(update_safe(user=user, chip_amount=bet, winning_status=False))
                    else:
                        print('Player are tie..!')
                else:
                    print('Please make a valid bet..!')
            else:
                print(f'Your {user.get("safe")} safe is under the minimum table bet..!')
                break
    else:
        print('Invalid credentials..!')

main()
from scrapper import Scrapper as scr
from pass_check_bot import PasswordChecker

class Unique_command:
    def __init__(self) -> None:
        self.menu()

    def UnlockURL(self):
        url = input('Enter url to unlock: ')
        scr(url, by_force=True)
        return

    def CheckPassword(self):
        url = input('Enter url to Check Password: ')
        PC = PasswordChecker(url)
        PC.RunAway()
        password_ = PC.secret_pass

        if password_ == 'NotFound':
            print('Not found Check it manually...')
            return
        else:
            print('password: ', password_)
            print('output password is found but we can\'t update it in the file without databases')
        return
    
    def menu(self):
        print('1 - Unlock URL')
        print('2 - Check Password')
        print('0 - Exit')
        while True:
            command = int(input('Enter Option: '))

            if command == 0: exit()
            
            elif command == 1:
                self.UnlockURL()
                break

            elif command == 2:
                self.CheckPassword()
                break

            else:
                print('Select one of option number...')


Unique_command()
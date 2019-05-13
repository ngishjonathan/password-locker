#!/usr/bin/env python3.6

from password import Password

def create_password(flo,me,beat,joby):

    new_password = Password(flo,me,beat,joby)
    return new_password

def save_passwords(password):

    password.save_password()

def del_password(password):

    password.delete_password()

def find_password(user_name):

    return Password.find_by_user_name(user_name)

def check_existng_passwords(user_name):

    return Password.password_exist(user_name) 

def display_passwords():

    return Password.display_passwords() 


def main():
    print("Hello,What is your name?")
    user_name = input()

    print(f"Hello{user_name}.what would u like to do?"
    print('\n')

    while True:
        print("Use these short codes : cc - create a new password, dc - display password, fc -find a password, ex -exit the password list ")
        
        short_code = input().lower()

        if short_code == 'cc'
            print("New Password")
            print("-"*10)

            print("first_name")
            f_name = input()

            print("last_name")
            last_name = input()

            print("user_name")
            u_user_name = input()

            print("password")
            p_password = input()

             save_passwords(create_password(f_name,l_name,u_user_name,p_password))
                            print ('\n')
                            print(f"New password {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_passwords():
                                    print("Here is a list of all your passwords")
                                    print('\n')

                                    for password in display_passwords():
                                        print(f"{pasword.first_name} {password.last_name} {password.user_name} {password.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any passwords saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_number = input()
                            if check_existing_passwords(search_user_name):
                                    search_password = find_password(search_user_name)
                                    print(f"{search_password.first_name} {search_password.last_name}")
                                    print('-' * 20)

                                    print(f"user_name.......{search_password.user_name}")
                                    print(f"password.......{search_password.password}")
                            else:
                                    print("That password does not exist")

                    elif short_code == "ex":
                            print("Bye user_name")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
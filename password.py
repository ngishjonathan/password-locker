class Password:


    password_list = []

    def save_Password(self):

        Password.password_list.append(self)

    def delete_password(self):

        Password.password_list.remove(self)


    def __init__(self,first_name,last_name,user_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
 
    @classmethod
    def find_by_user_name(cls,user_name):

        for Password in cls.password_list:
            if Password.user_name == user_name:
                return Password

    @classmethod
    def password_exist(cls,user_name):

        for password in cls.password_list:
            if password.user_name == user_name:
                return True

    @classmethod
    def display_passwords(cls):

        return cls.password_list




        return False        
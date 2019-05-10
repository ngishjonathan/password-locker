class Password:


    password_list = []

    def save_Password(self):

        Password.password_list.append(self)

    def __init__(self,first_name,second_name,user_name,password):

        self.first_name = first_name
        self.second_name = second_name
        self.user_name = user_name
        self.password = password
 

    
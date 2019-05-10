import unittest
from password import Password

class TestPassword(unittest.TestCase):

   

    def setUp(self):

        self.new_password = Password("james","nyoro","jymo","3114")

    def test_init(self):

        self.assertEqual(self.new_password.first_name,"james")
        self.assertEqual(self.new_password.second_name,"nyoro")
        self.assertEqual(self.new_password.user_name,"jymo")
        self.assertEqual(self.new_password.password,"3114")

    def test_save_password(self):

        self.new_password.save_Password()
        self.assertEqual(len(Password.password_list),1)



    def test_save_multiple_contact(self):

        self.new_password.save_Password() 
        test_password = Password("Test","flo","boel","flock","7350")
        self.assertEqual(len(Password.password_list),2)

                  

if __name__ ==  '__main__':
        unittest.main()

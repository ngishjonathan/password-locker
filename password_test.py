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



    def test_save_multiple_password(self):

        self.new_password.save_Password() 
        test_password = Password("Test","flo","boel","flock","7350")
        self.assertEqual(len(Password.password_list),2)


    def tearDown(self):

        Password.password_list = []  

    def test_save_multiple_password(self):

        self.new_password.save_Password()
        test_password = Password("flo","boel","flock","7350")                
        test_password.save_Password()
        self.assertEqual(len(Password.password_list),2)

    def test_save_multiple_password(self): 

        self.new_password.save_Password()
        test_password = Password("flo","boel","flock","7350")
        test_password.save_Password()
        self.assertEqual(len(Password.password_list),2)

    def test_delete_password(self):

        self.new_password.save_Password()
        test_password = Password("flo","boel","flock","7350")
        test_password.save_Password()

        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)

    def test_find_password_by_user_name(self):

        self.new_password.save_Password()
        test_password = Password("flo","boel","flock","7350")
        test_password.save_Password()

        found_password = Password.find_by_user_name("flock")

        self.assertEqual(found_password.password,test_password.password)

    def test_password_exist(self):

        self.new_password.save_Password
        test_password = Password("flo","boel","flock","7350")
        test_password.save_Password()

        password_exist = Password.password_exist("flock")

        self.assertTrue(password_exist)

if __name__ ==  '__main__':
        unittest.main()

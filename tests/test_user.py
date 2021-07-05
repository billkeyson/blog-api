import unittest
from models.user_model import UserModel
class ProfileTests(unittest.TestCase):
    def test_add_user(self):
        add_user = UserModel.add_user("test",'password',"billkeyson@mail.com","billy",0,['freelancer','teacher'])
        self.assertIsNot(add_user,None)




if __name__ == "__main__":
    unittest.main(verbosity=2)

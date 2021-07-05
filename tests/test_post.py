import unittest
from models.post_model import PostModel

class PostTests(unittest.TestCase):
    def test_find_all_post(self):
        add_user = PostModel.find_all_post()
        self.assertIsInstance(add_user,list)


    def test_find_post_by_name(self):
        add_user = PostModel.find_post_by_name('test')
        self.assertIsInstance(add_user,dict)




if __name__ == "__main__":
    unittest.main(verbosity=2)

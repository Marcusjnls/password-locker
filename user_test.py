import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Marcus", "Jean-Louis", "marcusjnls", "password1234")

    def test_init(self):
        '''
        test_init test case to see if object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name, "Marcus")
        self.assertEqual(self.new_user.last_name, "Jean-Louis")
        self.assertEqual(self.new_user.user_name, "marcusjnls")
        self.assertEqual(self.new_user.password, "password1234")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() #saving the new user_list
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []

    def test_save_multiple_users(self):

        '''
        Check if we can save multiple user objects to our user_list
        '''
        
        self.new_user.save_user()
        test_user = User("Luke", "Skywalker", "darthvader", "iamyourfather")
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)


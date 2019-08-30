import unittest # Importing the unittest module
from User import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

        def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Marcus", "Jean-Louis", "marcusjnls", "password1234")
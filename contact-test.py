import unittest  # Importing the unittest module
from contact import Contact  # Importing the contact class


class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("Eva", "Maina", "0722811823", "evajohnson714@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name, "Eva")
        self.assertEqual(self.new_contact.last_name, "Maina")
        self.assertEqual(self.new_contact.phone_number, "0722811823")
        self.assertEqual(self.new_contact.email, "evajohnson714@gmail.com")

    def test_add_contact(self):
        '''
        test_add_contact test case to test if the contact object is added into
         the contact list
        '''
        self.new_contact.add_contact()  # adding the new contact
        self.assertEqual(len(Contact.contact_list), 1)

    def test_update_contact(self):
        '''
        test_update_contact test case to test if the contact
        object added is updated into the contact list
        '''
        self.new_contact.update_contact()  # adding the new contact
        self.assertEqual(len(Contact.contact_list), 1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Contact.contact_list = []

    def test_add_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.add_contact()  # Adding Record 1

            test_contact = Contact("Test", "user", "0712345678", "test@user.com")

            test_contact.add_contact()  # adding Record 2
            self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a
             contact from our contact list
            '''
            self.new_contact.add_contact()
            test_contact = Contact("Test", "user", "0712345678", "test@user.com")
            test_contact.add_contact()

            self.new_contact.delete_contact()  # Deleting a contact object
            self.assertEqual(len(Contact.contact_list), 1)

    def test_view_contact_by_number(self):
        self.new_contact.add_contact()
        test_contact = Contact("Test", "user", "0711223344", "test@user.com")
        test_contact.add_contact()

        view_contact = Contact.view_by_number("0711223344")

        self.assertEqual(view_contact.email, test_contact.email)


if __name__ == '__main__':
    unittest.main()

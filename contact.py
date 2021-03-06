class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = []  # Empty contact list

    def __init__(self, first_name, last_name, phone_number, email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def add_contact(self):

        # add_contact method saves contact objects into contact_list

        Contact.contact_list.append(self)

    def update_contact(self):

        # update_contact method updates contact objects added into contact_list

        Contact.contact_list.append(self)

    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

    @classmethod
    def view_by_number(cls, number):
        '''
        Method that takes in a number and returns a contact
        that matches that number.

        Contact of person that matches the number.
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact




















    


class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,phone_number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def add_contact(self):

        # save_contact method saves contact objects into contact_list

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
    def view_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact




        














        

""" Evet to refer later


new_contact = Contact("Eva","Maina","0722811823","evajohnson714@gmail.com")


print new_contact.first_name
print new_contact.last_name
print new_contact.phone_number
print new_contact.email


#Generaing my details in one statement
print "My name is ",new_contact.first_name, new_contact.last_name, \
",my phone number is",new_contact.phone_number, "and my email address is",new_contact.email


#Another way of dispalying in one a sentence
print "My name is %s %s" %(new_contact.first_name, new_contact.last_name), \
",my phone number is %s" %(new_contact.phone_number), "and my email address is %s" %(new_contact.email)
"""
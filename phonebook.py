from linkedlist import SingleLinkedList
from node import Node

class MissingPhoneNumberException(Exception):
    pass


class MissingNameException(Exception):
    pass


class Contact():
    ''' represents a contact in a phone book'''
    def __init__(self, cp=None, name=None, surname=None,
                 hp=None, wp=None, email=None, ha=None, fav=False):
        ''' (Contact) -> NoneType
        Constructs a contact for a phone book
        REQ: all inputs should be of type obj and fav should be bool
        and should include a name (first or last) and at least a number
        '''
        # create private instance variables
        self._cp = cp
        self._name = name
        self._surname = surname
        self._hp = hp
        self._wp = wp
        self._email = email
        self._ha = ha
        self._fav = fav

        # check if contact is missing a name by calling method in Contact class
        # and raise an exception so it's not included in this phone book
        if self.name_isempty():
            raise MissingNameException("This contact doesn't have a name")

        # check if contact is missing a number by calling method in Contact
        # class so it's not included
        if self.phone_isempty():
            raise MissingPhoneNumberException("contact has no phone number")

        # create setter and getter methods for all of these variables

    def set_cp(self, new_cp):
        '''(Contact, obj) -> NoneType
        sets a new cell phone number for this contact
        REQ: new_cp should either be a str or an int
        '''

        self._cp = new_cp

    def set_name(self, new_name):
        '''(Contact, str) -> NoneType
        sets a new first name for this contact
        REQ: new_name should be a str
        '''

        self._name = new_name

    def set_surname(self, new_surname):
        '''(Contact, str) -> NoneType
        sets a new last name for this contact
        REQ: new_surname should be a str
        '''
        self._surname = new_surname

    def set_hp(self, new_hp):
        '''(Contact, obj) -> NoneType
        sets a new home phone number for this contact
        REQ: new_hp should either be a str or an int
        '''

        self._hp = new_hp

    def set_wp(self, new_wp):
        '''(Contact, obj) -> NoneType
        sets a new work phone number for this contact
        REQ: new_wp should either be a str or an int
        '''

        self._wp = new_wp

    def set_email(self, new_email):
        '''(Contact, str) -> NoneType
        sets a new email for this contact
        REQ: new_email should be a str
        '''
        self._email = new_email

    def set_ha(self, new_ha):
        '''(Contact, obj) -> NoneType
        sets a new home address
        REQ: new_ha should be a str
        '''

        self._ha = new_ha

    def set_fav(self, new_fav):
        '''(Contact, bool) -> NoneType
        updates this contact as a favourite or nonfavourite
        REQ: new_fav should be a bool
        '''

        self._fav = new_fav

    def get_cp(self):
        '''(Contact) -> obj
        returns the contacts cell phone number
        '''
        return self._cp

    def get_name(self):
        '''(Contact) -> str
        returns the first name of the contact
        '''

        return self._name

    def get_surname(self):
        '''(Contact) -> str
        returns the last name of the contact
        '''
        return self._surname

    def get_hp(self):
        '''(Contact) -> obj
        returns the home phone number of this contact
        '''

        return self._hp

    def get_wp(self):
        '''(Contact) -> obj
        returns the contact's work phone number
        '''

        return self._wp

    def get_email(self):
        '''(Contact) -> str
        returns the contact's email address
        '''
        return self._email

    def get_ha(self):
        '''(Contact) -> str
        returns the contact's house address
        '''
        return self._ha

    def get_fav(self):
        '''(Contact) -> bool
        returns whether this contact is a favourite / nonfavourite
        '''
        return self._fav

    def get_primarynumber(self):
        '''(Contact) -> obj
        returns the contact's primary phone number. The first
        phone number available (not None) amongst cp, hp, and wp is the
        primary number
        '''
        # check if cell phone number is inserted to make it primary
        if (self._cp is not None):
            primary_number = self._cp
        # check if cell phone is not inserted and home phone is inserted
        elif (self._hp is not None):
            primary_number = self._hp
        # check if home phone is not inserted and work phone is inserted
        elif (self._wp is not None):
            primary_number = self._wp

        return primary_number

    def get_primarytype(self):
        '''(Contact) -> str
        returns the contact's primary phone type. The first
        phone number available (not None) amongst cp, hp, and wp is the
        primary type
        '''

        # check if cell phone number is inserted to make it primary
        if (self._cp is not None):
            primary_type = "Cell Phone"
        # check if cell phone is not inserted and home phone is inserted
        elif (self._hp is not None):
            primary_type = "Home Phone"
        # check if home phone is not inserted and work phone is inserted
        elif (self._wp is not None):
            primary_type = "Work Phone"

        return primary_type

    def name_isempty(self):
        ''' (Contact) -> bool
        checks iff first name and last name are included and returns True
        or else it returns False
        '''
        # see if first name and surname are none
        empty = (self._name is None) and (self._surname is None)
        return empty

    def phone_isempty(self):
        ''' (Contact) -> bool
        determines if Contact includes either cell phone, home phone, or
        work phone. If it doesn't include any of these then it should return
        False or else it's True
        '''

        # see if first name and surname are none
        empty = ((self._cp is None) and (self._hp is None) and
                 (self._wp is None))
        return empty

    def identical(self, other):
        '''(Contact, Contact) -> bool
        checks iff all attributes of a contact are the same and returns
        True or else it returns False
        REQ: other is of type Contact only and should include at least a
        name and a number
        '''

        # check for equal first name
        equal_first_name = ((str(self.get_name())[0].upper() +
                            str(self.get_name())[1:].lower()) ==
                            (str(other.get_name())[0].upper() +
                             str(other.get_name())[1:].lower()))

        # check for equal last name
        equal_last_name = ((str(self.get_surname())[0].upper() +
                            str(self.get_surname())[1:].lower()) ==
                           (str(other.get_surname())[0].upper() +
                           str(other.get_surname())[1:].lower()))

        # check if both the first and last names are the same
        equal_name = equal_first_name and equal_last_name

        # check if primary number and type are the same
        equal_primary = ((self.get_primarytype() ==
                         other.get_primarytype()) and
                         (self.get_primarynumber() ==
                         other.get_primarynumber()))

        # check if cell phone numbers are the same
        equal_cp = (self.get_cp() == other.get_cp())

        # check if home phone numbers are the same
        equal_hp = (self.get_hp() == other.get_hp())

        # check if work phone numbers are the same
        equal_wp = (self.get_wp() == other.get_wp())

        # check if email addresses are the same
        equal_email = (self.get_email() == other.get_email())

        # check if home addresses are the same
        equal_ha = (self.get_ha() == other.get_ha())

        # check if both contacts are listed as favourite
        equal_fav = (self.get_fav() == other.get_fav())

        # both contacts are identical if they have all equal attributes
        is_identical = (equal_name and equal_primary and equal_cp and
                        equal_hp and equal_wp and equal_email and
                        equal_ha and equal_fav)

        return is_identical

    def __eq__(self, other):
        '''(Contact, Contact) -> bool
        checks iff two contacts are the same and returns True iff they are.
        Two contacts are the same if they have same first and last name (if
        it exists) and same primary phone number of the same type
        REQ: other is of type Contact only and should include at least a
        name and a number
        '''

        # check for equal first name
        equal_first_name = ((str(self.get_name())[0].upper() +
                            str(self.get_name())[1:].lower()) ==
                            (str(other.get_name())[0].upper() +
                                str(other.get_name())[1:].lower()))

        # check for equal last name
        equal_last_name = ((str(self.get_surname())[0].upper() +
                            str(self.get_surname())[1:].lower()) ==
                           (str(other.get_surname())[0].upper() +
                               str(other.get_surname())[1:].lower()))

        # check if both the first and last names are the same
        equal_name = equal_first_name and equal_last_name

        # check if primary number and type are the same
        equal_number = (self.get_primarytype() == other.get_primarytype()
                        ) and (self.get_primarynumber() ==
                               other.get_primarynumber())

        # both contacts are equal if they have same name and number
        equal = equal_name and equal_number
        return equal


class PhoneBook(SingleLinkedList):
    ''' represents a phone book class'''
    def __init__(self, contact=None):
        ''' (PhoneBook, Contact) -> Nonetype
        constructs a phone book with contacts
        REQ: if contact is inputed it should have a name and a number
        and should be of type Contact
        '''
        SingleLinkedList.__init__(self)
        # create private instance variable for contact
        self._contact = contact

        # check if contact was inputted but didn't contain a name or number
        if self._contact is not None:
            # check if contact is missing a name by calling method
            # in Contact class and raise an exception so it's not
            # included in this phone book
            if contact.name_isempty():
                raise MissingNameException("This contact doesn't have a name")

            # check if contact is missing a number by calling method in Contact
            # class so it's not included
            if contact.phone_isempty():
                raise MissingPhoneNumberException("contact has no number")

            # then add this contact into the phonebook
            self.add_first(self._contact)

    # helper method for efficiency and readability
    def get_prev_prev_node(self, index):
        '''(PhoneBook, int) -> Node
        returns the previous previous node with the given index
        REQ: index should be an int
        '''

        # keep count of nodes in list
        previous_index = 0
        # start position at head to end at tail
        current = self._head
        # keep iterating until at end of list or when count is equal the index
        # of the previous node
        while ((current is not None) and (previous_index < index - 2)):
            # keep moving to next node until previous_index is found
            current = current.get_next()
            # move to next index
            previous_index += 1

        return current

    # helper method for efficiency and readability
    def get_prev_node(self, index):
        '''(PhoneBook, int) -> Node
        returns the previous node with the given index
        REQ: index should be an int
        '''

        # keep count of nodes in list
        previous_index = 0
        # start position at head to end at tail
        current = self._head
        # keep iterating until at end of list or when count is equal the index
        # of the previous node
        while ((current is not None) and (previous_index < index - 1)):
            # keep moving to next node until previous_index is found
            current = current.get_next()
            # move to next index
            previous_index += 1

        return current

    # helper method for efficiency / readability
    def count_occurrences(self, contact):
        '''(PhoneBook, Contact) -> int
        counts occurrences of gives name in the phone book and returns the
        amount of occurrences
        REQ: contact should be of type Contact and should include at least
        a name and a number
        '''

        # check if contact has last name to order it
        if contact.get_surname() is not None:
            # we will consider last name alphabetically
            name = contact.get_surname()
        # else use the contact's first name to order it
        else:
            # consider first name alphabetically
            name = contact.get_name()

        # start at head until it reaches tail
        current = self._head
        # to count occurrence of name
        occurrence = 0
        # keep iterating until it reaches tail or when spot is found
        while (current is not None):
            # check if there's a last name
            if (current.get_element().get_surname() is not None):
                # check if name's already in the list
                if (((current.get_element().get_surname())[0].upper() +
                        (current.get_element().get_surname()[1:].lower())) ==
                        (name[0].upper() + (name[1:].lower()))):
                            # keep track of amount of occurrences
                            occurrence += 1

            # else just compare the current first name
            else:
                # check if name's already in the list
                if (((current.get_element().get_name())[0].upper() +
                        (current.get_element().get_name()[1:].lower())) ==
                        (name[0].upper() + (name[1:].lower()))):
                            occurrence += 1
            # point to next node
            current = current.get_next()

        return occurrence

    # helper method for efficiency / readability
    def find_index(self, contact):
        '''(PhoneBook, Contact) -> int
        returns the index of where the name is first found
        REQ: contact should be of type Contact and should include at least
        a name and a number
        '''

        # check if contact has last name to order it
        if contact.get_surname() is not None:
            # we will consider last name alphabetically
            name = contact.get_surname()
        # else use the contact's first name to order it
        else:
            # consider first name alphabetically
            name = contact.get_name()

        # start at head until it reaches tail
        current = self._head
        # to keep track of index where name is found
        index = 0
        # found becomes True when name's found
        found = False
        # keep iterating until it reaches tail or when spot is found
        while ((current is not None) and (not found)):
            # check if there's a last name
            if (current.get_element().get_surname() is not None):
                # check if name's already in the list
                if (((current.get_element().get_surname())[0].upper() +
                        (current.get_element().get_surname()[1:].lower())) ==
                        (name[0].upper() + (name[1:].lower()))):
                            # if name is found
                            found = True

            # else just compare the current first name
            else:
                # check if name's already in the list
                if (((current.get_element().get_name())[0].upper() +
                        (current.get_element().get_name()[1:].lower())) ==
                        (name[0].upper() + (name[1:].lower()))):
                            # if name is found
                            found = True
            # point to next node
            current = current.get_next()
            # keep track of index
            index += 1

        return index - 1

    def add(self, contact):
        ''' (PhoneBook, Contact) -> NoneType
        adds contact to the phone book based on alphabetical order. If both
        the first name and surname is provided for the contact, then surname
        is the basis for inserting the contact in the right place in
        alphabetical order, otherwise first name is used
        REQ: contact should be of type Contact and contain atleast a name
        and a number
        '''
        # check if contact is missing a name by calling method in Contact class
        # and raise an exception so it's not included in this phone book
        if contact.name_isempty():
            raise MissingNameException("This contact doesn't have a name")

        # check if contact is missing a number by calling method in Contact
        # class so it's not included
        if contact.phone_isempty():
            raise MissingPhoneNumberException("contact doesn't have a number")

        # create a node with new contact
        node = Node(contact, None)
        # count occurrences if same name exist, use helper method
        occurrence = self.count_occurrences(contact)
        # check if occurrence exist
        if occurrence > 0:
            # find where the index of where the name is found with
            # helper method
            find = self.find_index(contact)
            # this is where the new node will be inserted, use helper method
            insertion_index = find + occurrence
            # get the previous node, use helper method
            prev_node = self.get_prev_node(insertion_index)
            # get next node after new node
            next_node = prev_node.get_next()
            # set it new node as next
            prev_node.set_next(node)
            node.set_next(next_node)
            # check if new node is being inserted last and is pointing to None
            if next_node is None:
                # it becomes the new tail since it's last
                self._tail = node

            # add size
            self._size += 1

        # if duplicate names don't exist
        else:
            # check if contact has last name to order it
            if contact.get_surname() is not None:
                # we will consider last name alphabetically
                name = contact.get_surname()
            # else use the contact's first name to order it
            else:
                # consider first name alphabetically
                name = contact.get_name()

            # also check if place is found to insert new contact
            found = False
            # keep track of single linked list index
            index = 0
            # start curr_1 as head node to iterate
            curr_1 = self._head
            # keep iterating until it reaches tail or when spot is found
            while ((curr_1 is not None) and (not found)):
                # check if there's a last name
                if (curr_1.get_element().get_surname() is not None):
                    # check if new name is less than phone book
                    # names alphabetically
                    if (((curr_1.get_element().get_surname())[0].upper() +
                            (curr_1.get_element().get_surname()[1:].lower())) >
                            (name[0].upper() + (name[1:].lower()))):
                                # spot is found
                                found = True

                # else just compare the curr_1 first name
                else:
                    # check if new name is less than phone book
                    # names alphabetically
                    if (((curr_1.get_element().get_name())[0].upper() +
                            (curr_1.get_element().get_name()[1:].lower())) >
                            (name[0].upper() + (name[1:].lower()))):
                                # spot is found
                                found = True

                # if not found keep checking next contacts in list
                curr_1 = curr_1.get_next()
                # keep adding index by one to show current index in list
                index += 1

            # if there's not an identical name but a spot is found
            if found:

                # check if it's going to be added to the front since it only
                # counted one person in the list
                if index == 1:
                    # add new contact at the beginning as the new head
                    self.add_first(contact)

                # if it's not going to be first in list
                else:
                    # call helper method to obtain previous previous
                    # node. used for efficiency/readability
                    curr_2 = self.get_prev_prev_node(index)
                    # curr_1 was after curr_2
                    curr_1 = curr_2.get_next()
                    # set previous node to new node
                    curr_2.set_next(node)
                    # set new node to the next node
                    node.set_next(curr_1)
                    # increase size
                    self._size += 1
            # if spot wasn't found then add this to the end
            else:
                # add contact to end of list
                self.add_last(contact)

    def remove(self, contact):
        '''(PhoneBook, Contact) -> Contact
        removes the given contact iff found or else it returns None
        REQ: contact should be of type Contact and should include at least
        a name and a number
        '''

        # check if contact is missing a name by calling method in Contact class
        # and raise an exception so it's not included in this phone book
        if contact.name_isempty():
            raise MissingNameException("This contact doesn't have a name")

        # check if contact is missing a number by calling method in Contact
        # class so it's not included
        if contact.phone_isempty():
            raise MissingPhoneNumberException("contact has no phone number")

        # set current to start at head to iterate until tail
        current = self._head
        # keep track if given contact is found in list
        found = False
        # keep track of index
        index = 0
        # iterate until found or until end of list
        while ((current is not None) and (not found)):
            # check if both contacts are identical with method in Contact
            if current.get_element().identical(contact):
                # then contact is found
                found = True
            # keep moving through list
            current = current.get_next()
            # keep track while moving through out list
            index += 1

        # if there's only one contact in the list
        if found and self._size == 1:
            # get the choice of contact to be removed
            removed_contact = self.get_prev_node(index)
            # set it next to none to be removed
            removed_contact.set_next(None)
            removed_contact = removed_contact.get_element()
            # decrease size
            self._size -= 1
            self._head = None
            self._tail = None

        # if duplicate contact is found and there's more than one contact
        elif found:
            # the given contact is before the current node
            removed_contact = self.get_prev_node(index)
            # check if contact to be removed is at the head
            if removed_contact is self._head:
                # we are removing first contact in list
                removed_contact = self.remove_first()
            # check if contact is at tail
            elif removed_contact is self._tail:
                # previous node is twice before current index
                prev_node = self.get_prev_prev_node(index)
                # next node is actually the current node
                next_node = current
                # set previous node to next node
                prev_node.set_next(next_node)
                # set previous node as tail
                self.set_tail(prev_node)
                # set given contact next to None to be removed
                removed_contact.set_next(None)
                removed_contact = removed_contact.get_element()
                # decrement the list size
                self._size -= 1

            # if it's not the head or the tail
            else:
                # previous node is twice before current index
                prev_node = self.get_prev_prev_node(index)
                # next node is actually the current node
                next_node = current
                # set previous node to next node
                prev_node.set_next(next_node)
                # set given contact next to None to be removed
                removed_contact.set_next(None)
                removed_contact = removed_contact.get_element()
                # decrement the list size
                self._size -= 1

        # if it's not found then contact is None
        else:
            removed_contact = None

        return removed_contact

    def show_fav_list(self):
        '''(PhoneBook) -> list of str
        returns the list of all the names that are labeled as a favourite
        contact and If both the surname and first name for a contact had
        been included only the surname, otherwise the first name, is returned
        '''
        # create empty list to append favourite contacts
        fav_list = []
        # start at head to iterate until tail
        current = self._head
        # keep iterating until it reaches the end of list
        while (current is not None):
            # only if it was set as a favourite contact
            if current.get_element().get_fav() is True:
                # check if they have a last name to add it
                if current.get_element().get_surname() is not None:
                    # add those favourite contacts by last name
                    fav_list.append(current.get_element().get_surname())
                # then just include their first names
                else:
                    # add those favourite contacts by first name
                    fav_list.append(current.get_element().get_name())
            # point to next node
            current = current.get_next()

        return fav_list

    def toronto_phone(self):
        '''(PhoneBook) -> tuple of PhoneBook
        returns a tuple of a phone book where one contains the contacts
        who start with "416" and other starts with "647"
        '''
        # create both phonebooks starting with "416" and "647"
        phonebook_416 = PhoneBook()
        phonebook_647 = PhoneBook()

        # begin at start of list and end at tail
        current = self._head
        # keep going until the end
        while (current is not None):
            # check if it's a number beginning with 416
            if (str(current.get_element().get_primarynumber())[:3] == "416"):
                # add those contacts
                phonebook_416.add(current.get_element())
            # check if it's a number beginnging with 647
            elif (str(current.get_element().get_primarynumber())[:3] == "647"):
                # add those contacts
                phonebook_647.add(current.get_element())
            # move to next node
            current = current.get_next()

        return (phonebook_416, phonebook_647)

    def reversed_phonebook(self):
        '''(PhoneBook) -> PhoneBook
        returns a phonebook reversed in alphabetical order which is listed
        in descending order (i.e z to a)
        '''
        # initialize a reversed phone book
        reverse = PhoneBook(self._head.get_element())
        # start after head
        current = self._head.get_next()
        # keep going until end of list
        while (current is not None):
            # add first until tail becomes head and head becomes tail
            reverse.add_first(current.get_element())
            # point to next node
            current = current.get_next()

        return reverse

    def sync_phonebook(self, old_phonebook):
        '''(PhoneBook, PhoneBook) -> NoneType
        This method merges the current phonebook with the given phonebook
        that is given as an input to this method. When these two
        phonebooks are merged, their alphabetical order should
        still be preserved
        REQ: only a valid phonebook of type PhoneBook should be passed in
        '''
        # start at head node to end at tail while searching old phonebook
        curr_1 = old_phonebook.get_head()
        # iterate until at the end of tail before current is None
        while (curr_1 is not None):
            # add all contacts from old phonebook to new phonebook
            self.add(curr_1.get_element())
            # set current to keep pointing to next node so it can eventually
            # reach tail
            curr_1 = curr_1.get_next()

        # now check for duplicates in the new phonebook to merge old contacts
        curr_2 = self._head
        # iterate list until next current node is at the end of list
        while (curr_2.get_next() is not None):
            # check if contacts are equal to each other with __eq__ method
            if curr_2.get_element().__eq__(curr_2.get_next().get_element()):
                # keep track of the soon to be next node after duplicate is
                # removed
                curr_2_next = curr_2.get_next().get_next()
                # remove the old contact to keep the new contact, where new
                # contact will always be before old since we added old after
                self.remove(curr_2.get_next().get_element())
                # set it next to next node after the removed node
                curr_2.set_next(curr_2_next)
                # don't move pointer incase there is another contact that is
                # the same in list after removing the old same contact
                curr_2 = curr_2
            # we can keep checking for duplicate contacts
            else:
                # move to next node
                curr_2 = curr_2.get_next()

    def group_remove(self, remove_list):
        '''(PhoneBook, list of Contact) -> NoneType
        removes the contacts which are given in a list from the phone book
        REQ: remove_list should only contain list of type Contact and
        each contact should at least contain a name and a number
        '''

        # use a for loop to find all contacts in list and remove them
        for contact in remove_list:
            # remove the contacts by using remove method in PhoneBook class
            self.remove(contact)

    def get_sublist(self, letter):
        '''(PhoneBook, str) -> PhoneBook
        returns a phonebook where the contacts’ name starts
        with the given letter
        REQ: letter should only be a letter given as a str
        '''
        # create a phone book to store contacts that start with given letter
        phonebook_letter = PhoneBook()

        # set current as start of the list to search until the end
        current = self._head
        # use while loop until at the end of list which is before tail points
        # to None
        while (current is not None):
            # check if the contact has a last name and if it starts with the
            # given letter
            if current.get_element().get_surname() is not None:
                # compare the last names with the given letter
                if ((current.get_element().get_surname())[0].upper() ==
                        letter.upper()):
                            # add the contacts that have their last
                            # names beginning with the given letter
                            phonebook_letter.add(current.get_element())
                # just compare the first name
            elif current.get_element().get_surname() is None:
                # compare the first names with the given letter
                if ((current.get_element().get_name())[0].upper() ==
                        letter.upper()):
                            # add the contacts that have their first
                            # names beginning with the given letter
                            phonebook_letter.add(current.get_element())
            # keep moving pointer to next node
            current = current.get_next()

        return phonebook_letter

    def get_housemate(self, home_phone):
        '''(PhoneBook, obj) -> PhoneBook
        returns a phonebook containing all the
        contacts, who live in the same house and share the same
        home phone number
        REQ: home_phone should either be a str or an int
        '''
        # create a phone book to obtain all housemates with same home number
        phonebook_housemate = PhoneBook()

        # set current as start of the list to search until the end
        current = self._head
        # iterate until current reaches tail
        while (current is not None):
            # make sure home phone isn't none
            if home_phone is not None:
                # check if contact has same house number
                if str(current.get_element().get_hp()) == str(home_phone):
                    # add this contact as a housemate
                    phonebook_housemate.add(current.get_element())

            # move pointer to next node until it reaches tail
            current = current.get_next()

        return phonebook_housemate

    def rearrange_phonebook(self):
        '''(PhoneBook) -> NoneType
        this method rearranges the phonebook in a way that all the
        favourite contacts are in the front of the phonebook. After
        rearranging the phonebook, both the favourite and nonfavourite
        contacts should be in an alphabetical order
        '''

        # set curr_1 as head of list to loop until end of list
        curr_1 = self._head
        # iterate until curr_1 is at the end of list
        while (curr_1 is not None):
            # check if contact is listed as a favourite to insert at front
            # of list but it still won't be alphabetically correct
            if curr_1.get_element().get_fav() is True:
                # keep position of next node before removing current node
                # to add to front
                current_next = curr_1.get_next()
                # use remove method to remove node
                self.remove(curr_1.get_element())
                # add this favourite contact first
                self.add_first(curr_1.get_element())
                # set curr_1 to point to next node
                curr_1 = current_next

            else:
                # keep moving pointer to point to next node
                curr_1 = curr_1.get_next()

        # now we have fav contacts at front of list but they're not in
        # alphabetical order since we added it first, we have to add it first
        # again for it to be in alphabetical order

        # set curr_2 as head of list to loop until end of list
        curr_2 = self._head
        # iterate until curr_2 is at the end of list
        while (curr_2 is not None):
            # check if contact is listed as a favourite to insert at front
            # of list but it still won't be alphabetically correct
            if curr_2.get_element().get_fav() is True:
                # keep the position of the next node before removing
                # curr_2 node
                current_next_2 = curr_2.get_next()
                # remove the curr_2 node to add it to the front
                self.remove(curr_2.get_element())
                # add it to front of list to order it alphabetically
                self.add_first(curr_2.get_element())
                # point to the next node to keep iterating
                curr_2 = current_next_2

            else:
                # keep moving pointer to point to next node
                curr_2 = curr_2.get_next()


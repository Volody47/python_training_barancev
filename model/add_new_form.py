from sys import maxsize


class AddNewForm:
    def __init__(self, first_name=None, last_name=None, address=None, email=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 all_phones_from_home_page=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               or self.first_name is None or other.first_name is None or self.first_name == other.first_name\
               or self.last_name is None or other.last_name is None or self.last_name == other.last_name\
               or self.address is None or other.address is None and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
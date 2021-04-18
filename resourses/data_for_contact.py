from model.add_new_form import AddNewForm
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_contact_data = [AddNewForm(first_name="", last_name="", address="", email="")] + [
    AddNewForm(first_name=random_string("first_name:", 10), last_name=random_string("last_name:", 10), address=random_string("address:", 10), email=random_string("email:", 10))
    for i in range(5)
]
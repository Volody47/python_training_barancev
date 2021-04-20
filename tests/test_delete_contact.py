from model.add_new_form import AddNewForm
from random import randrange


def test_delete_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(AddNewForm(first_name="Vladimir"))
    old_contacts = app.contact.get_contact_list_version2()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list_version2()
    assert len(old_contacts) - 1 == app.contact.count_contact()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

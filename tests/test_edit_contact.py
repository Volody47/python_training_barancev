from model.add_new_form import AddNewForm
from random import randrange

def test_edit_contact_first_name(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(AddNewForm(first_name="Vladimir"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = AddNewForm(first_name="Vlad")
    app.contact.edit_contact_by_index(index, contact)
    contact.id = old_contacts[index].id
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count_contact()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=AddNewForm.id_or_max) == sorted(new_contacts, key=AddNewForm.id_or_max)


# def test_edit_contact_address(app):
#     if app.contact.count_contact() == 0:
#         app.contact.create_new_contact(AddNewForm(address="spb"))
#     app.contact.edit_first_contact(AddNewForm(address="Chicago"))

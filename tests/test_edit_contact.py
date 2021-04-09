from model.add_new_form import AddNewForm

def test_edit_contact_first_name(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(AddNewForm(first_name="Vladimir"))
    old_contacts = app.contact.get_contact_list()
    contact = AddNewForm(first_name="Vlad")
    app.contact.edit_first_contact(contact)
    contact.id = old_contacts[0].id
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=AddNewForm.id_or_max) == sorted(new_contacts, key=AddNewForm.id_or_max)


# def test_edit_contact_address(app):
#     if app.contact.count_contact() == 0:
#         app.contact.create_new_contact(AddNewForm(address="spb"))
#     app.contact.edit_first_contact(AddNewForm(address="Chicago"))

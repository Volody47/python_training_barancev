from model.add_new_form import AddNewForm


def test_delete_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(AddNewForm(first_name="Vladimir"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count_contact()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

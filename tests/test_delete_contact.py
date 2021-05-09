from model.add_new_form import AddNewForm
import random


def test_delete_contact(app, db):
    if db.get_contact_list() == 0:
        app.contact.create_new_contact(AddNewForm(first_name="Vladimir"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count_contact()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

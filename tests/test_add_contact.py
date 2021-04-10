# -*- coding: utf-8 -*-
from model.add_new_form import AddNewForm



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = AddNewForm(first_name="Vladimir", last_name="Sharapov", address="spb", email="test@gmail.com")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contact()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=AddNewForm.id_or_max) == sorted(new_contacts, key=AddNewForm.id_or_max)

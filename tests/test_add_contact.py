# -*- coding: utf-8 -*-
from model.add_new_form import AddNewForm
from resourses.data_for_contact import test_contact_data
import pytest


#@pytest.mark.parametrize("contact", test_contact_data, ids=[repr(x) for x in test_contact_data])
def test_add_contact(app, db, json_contact):
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contact()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=AddNewForm.id_or_max) == sorted(new_contacts, key=AddNewForm.id_or_max)

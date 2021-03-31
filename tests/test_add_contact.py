# -*- coding: utf-8 -*-
from model.add_new_form import AddNewForm



def test_add_contact(app):
    app.contact.create_new_contact(AddNewForm(first_name="Vladimir", last_name="Sharapov", address="spb", email="test@gmail.com"))


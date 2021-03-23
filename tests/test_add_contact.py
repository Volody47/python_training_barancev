# -*- coding: utf-8 -*-
from model.add_new_form import AddNewForm



def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_page()
    app.contact.create_new_contact(AddNewForm(first_name="Vladimir", last_name="Sharapov", address="spb", email="test@gmail.com"))
    app.contact.return_to_home_page()
    app.session.logout()


# -*- coding: utf-8 -*-
import pytest
from model.add_new_form import AddNewForm
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_add_new_page()
    app.create_new_contact(AddNewForm(first_name="Vladimir", last_name="Sharapov", address="spb", email="test@gmail.com"))
    app.return_to_home_page()
    app.session.logout()


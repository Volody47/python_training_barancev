from model.add_new_form import AddNewForm

def test_edit_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(AddNewForm(first_name="Vlad"))
    app.session.logout()

def test_edit_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(AddNewForm(address="Chicago"))
    app.session.logout()
from model.add_new_form import AddNewForm

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(AddNewForm(first_name="Vladimir", last_name="Sharapov", address="spb", email="test@gmail.com"))
    app.session.logout()
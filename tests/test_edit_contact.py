from model.add_new_form import AddNewForm

def test_edit_contact_first_name(app):
    app.contact.edit_first_contact(AddNewForm(first_name="Vlad"))

def test_edit_contact_address(app):
    app.contact.edit_first_contact(AddNewForm(address="Chicago"))

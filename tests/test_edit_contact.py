from model.add_new_form import AddNewForm

def test_edit_contact_first_name(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(AddNewForm(first_name="Vladimir"))
    app.contact.edit_first_contact(AddNewForm(first_name="Vlad"))


def test_edit_contact_address(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(AddNewForm(address="spb"))
    app.contact.edit_first_contact(AddNewForm(address="Chicago"))

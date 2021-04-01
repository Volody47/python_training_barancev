from model.add_new_form import AddNewForm


def test_delete_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(AddNewForm(first_name="Vladimir"))
    app.contact.delete_first_contact()

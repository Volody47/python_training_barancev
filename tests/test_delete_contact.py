


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_home_page()
    app.contact.delete_first_contact()
    app.contact.open_home_page()
    app.session.logout()
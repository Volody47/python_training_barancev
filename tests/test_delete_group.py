

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.delete_first_group()
    app.group.return_to_groups_page()
    app.session.logout()
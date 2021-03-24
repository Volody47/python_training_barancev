from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_first_group(Group(name="gfsdgsdhs", header="sdfsvds", footer="sdssvs"))
    app.group.return_to_groups_page()
    app.session.logout()
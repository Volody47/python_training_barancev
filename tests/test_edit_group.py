from model.group import Group

def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New group", header="sdfsvds", footer="sdssvs"))
    app.session.logout()

def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New group", header="sdfsvds", footer="sdssvs"))
    app.session.logout()
from model.group import Group

def test_edit_group_name(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="gfsdgsdhs"))
    app.group.edit_first_group(Group(name="New group"))


def test_edit_group_header(app):
    if app.group.count_group() == 0:
        app.group.create(Group(header="sdfsvds"))
    app.group.edit_first_group(Group(header="New header"))

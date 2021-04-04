from model.group import Group

def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count_group() == 0:
        app.group.create(Group(name="gfsdgsdhs"))
    app.group.edit_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count_group() == 0:
        app.group.create(Group(header="sdfsvds"))
    app.group.edit_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

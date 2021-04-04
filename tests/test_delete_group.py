from model.group import Group


def test_delete_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count_group() == 0:
        app.group.create(Group(name="gfsdgsdhs", header="sdfsvds", footer="sdssvs"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

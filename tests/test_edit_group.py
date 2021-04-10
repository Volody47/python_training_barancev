from model.group import Group
from random import randrange

def test_edit_group_name(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="gfsdgsdhs"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count_group()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count_group() == 0:
#         app.group.create(Group(header="sdfsvds"))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(header="New header")
#     group.id = old_groups[0].id
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == app.group.count_group()
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

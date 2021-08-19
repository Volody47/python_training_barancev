from model.group import Group
import random

def test_edit_group_name(app, db):
    if db.get_group_list() == 0:
        app.group.create(Group(name="gfsdgsdhs"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_changes_for_group = Group(name="New group")
    app.group.edit_group_by_id(group.id, new_changes_for_group)
    group.id = old_groups[group].id
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count_group()
    old_groups[group] = group
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

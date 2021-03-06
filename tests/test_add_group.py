# -*- coding: utf-8 -*-
from model.group import Group
from resourses.data_for_group import constant as test_group_data
import pytest


#@pytest.mark.parametrize("group", test_group_data, ids=[repr(x) for x in test_group_data])
def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    assert len(old_groups) + 1 == app.group.count_group()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == app.group.count_group()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




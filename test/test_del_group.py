import random


def test_del_group(app):
    if len(app.groups.get_group_list()) == 0:
        app.groups.add_new_group("new group")
    old_list = app.groups.get_group_list()
    app.groups.delete_first_group(old_list)
    new_list = app.groups.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    assert sorted(old_list) == sorted(new_list)

def test_add_group(app, xlsx_groups):
    group = xlsx_groups
    old_list = app.groups.get_group_list()
    app.groups.add_new_group("my group")
    new_list = app.groups.get_group_list()
    old_list.append("my group")
    assert sorted(old_list) == sorted(new_list)

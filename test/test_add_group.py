def test_add_group(app, xlsx_groups):
    old_list = app.group.get_group_list()
    app.group.add_new_group(xlsx_groups)
    new_list = app.group.get_group_list()
    old_list.append(xlsx_groups)
    assert sorted(old_list) == sorted(new_list)

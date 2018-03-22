from random import randrange


def test_delete_some_group(app):
    app.group.ensure_group_created('test group')
    old_list = app.group.get_group_list()
    index = randrange(len(old_list))
    app.group.delete_group_by_index(index)
    new_list = app.group.get_group_list()
    old_list[index:index+1] = []
    assert sorted(old_list) == sorted(new_list)

def create_groups(apps, schema_migration):
    User = apps.get_model('authentification', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    add_project = Permission.objects.get(codename='add_project')
    edit_project = Permission.objects.get(codename='change_project')
    delete_project = Permission.objects.get(codename='delete_project')
    view_project = Permission.objects.get(codename='view_project')

    add_user = Permission.objects.get(codename='add_user')
    change_user = Permission.objects.get(codename='change_user')
    edit_user = Permission.objects.get(codename='delete_user')
    view_user = Permission.objects.get(codename='view_user')

    add_task = Permission.objects.get(codename='add_task')
    edit_task = Permission.objects.get(codename='change_task')
    delete_task = Permission.objects.get(codename='delete_task')
    view_task = Permission.objects.get(codename='view_task')

    add_group = Permission.objects.get(codename='add_group')
    view_group = Permission.objects.get(codename='view_group')
    change_group = Permission.objects.get(codename='change_group')

    add_leave = Permission.objects.get(codename='add_leave')
    view_leave = Permission.objects.get(codename='view_leave')
    change_leave = Permission.objects.get(codename='change_leave')
    delete_leave = Permission.objects.get(codename='delete_leave')

    manager_permissions = [
        add_project,
        edit_project,
        delete_project,
        view_project,
        add_user,
        change_user,
        view_user,
        edit_user,
        add_task,
        edit_task,
        delete_task,
        view_task,
        add_group,
        view_group,
        change_group,
        add_leave,
        view_leave,
        change_leave,
        delete_leave
    ]

    employee_permission = [
        view_project,
        add_task,
        edit_task,
        delete_task,
        view_task,
        add_leave,
        delete_leave
    ]

    manager = Group(name='manager')
    manager.save()

    manager.permissions.set(manager_permissions)

    employee = Group(name='employer')
    employee.save()
    employee.permissions.set(employee_permission)

    for user in User.objects.all():
        if user.user_role == 'MANAGER':
            manager.user_set.add(user)
        if user.user_role == 'EMPLOYER':
            employee.user_set.add(user)

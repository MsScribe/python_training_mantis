from model.mantis import MantisProject


def test_add_project(app):
    mantis = MantisProject(projectname=app.mantis.random_string("name_", 10), description=app.mantis.random_string("description_", 20))
    app.mantis.open_project_page()
    old_mantis = app.mantis.get_project_list()
    if app.mantis.get_existing_project(mantis.projectname):
        app.mantis.delete_project_mantis(mantis.projectname)
        old_mantis = app.mantis.get_project_list()
    app.mantis.open_create_project_page()
    app.mantis.create_project_mantis(mantis)
    old_mantis.append(mantis)
    app.mantis.open_project_page()
    new_mantis = app.mantis.get_project_list()
    assert sorted(old_mantis, key=MantisProject.id_or_max) == sorted(new_mantis, key=MantisProject.id_or_max)
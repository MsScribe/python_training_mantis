import random
from model.mantis import MantisProject


def test_delete_project(app):
    app.mantis.open_project_page()
    old_mantis = app.soap.get_project_list()
    if old_mantis == []:
        app.mantis.open_create_project_page()
        app.mantis.create_project_mantis(MantisProject(projectname=app.mantis.random_string("name_", 10), description=app.mantis.random_string("description_", 20)))
        app.mantis.open_project_page()
        old_mantis = app.soap.get_project_list()
    mantis = random.choice(old_mantis)
    app.mantis.delete_project_mantis(mantis.projectname)
    old_mantis.remove(mantis)
    app.mantis.open_project_page()
    new_mantis = app.soap.get_project_list()
    assert sorted(old_mantis, key=MantisProject.id_or_max) == sorted(new_mantis, key=MantisProject.id_or_max)
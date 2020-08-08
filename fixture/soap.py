from model.mantis import MantisProject
from suds.client import Client
from suds import WebFault


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        project_list = []
        for project in client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'], self.app.config['webadmin']['password']):
            project_list.append(MantisProject(projectname=project.name, description=project.description, id=project.id))
        return project_list
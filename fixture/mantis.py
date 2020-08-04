import string
import random
from model.mantis import MantisProject


class MantisHelper:
    def __init__(self, app):
        self.app = app

    mantis_cache = None

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_elements_by_link_text("Create New Project")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_xpath("//a[contains(text(),'Manage Projects')]").click()

    def open_create_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def create_project_mantis(self, project):
        wd = self.app.wd
        self.fill_project_data(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.mantis_cache = None

    def fill_project_data(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.projectname)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_project_list(self):
        wd = self.app.wd
        self.mantis_cache = []
        count = len(wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-2']/td[1]/a|//table[@class='width100']//tr[@class='row-1']/td[1]/a"))
        count = count + 1
        for i in range(2, count + 1):
            project_name = wd.find_element_by_xpath("//table[@class='width100']//tr[contains(@class,'row')]["+str(i)+"]/td[1]/a").text
            description = wd.find_element_by_xpath("//table[@class='width100']//tr[contains(@class,'row')]["+str(i)+"]/td[5]").text
            id = wd.find_element_by_xpath("//table[@class='width100']//tr[contains(@class,'row')]["+str(i)+"]//a[contains(@href,'manage_proj_edit_page')]").get_attribute("href").split('=')[-1]
            self.mantis_cache.append(MantisProject(projectname=project_name, description=description, id=id))
        return list(self.mantis_cache)

    def delete_project_mantis(self, name):
        wd = self.app.wd
        self.open_project_page()
        self.open_project(name)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def open_project(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@class='width100']//tr/td/a[contains(@href,'manage_proj_edit_page')][text()='" + name + "']").click()

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def comparator(self, e1, e2):
        return e1.text > e2.text

    def get_existing_project(self, project):
        wd = self.app.wd
        count = len(wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-2']/td[1]/a|//table[@class='width100']//tr[@class='row-1']/td[1]/a"))
        count = count + 1
        for i in range(2, count + 1):
            project_name = wd.find_element_by_xpath("//table[@class='width100']//tr[contains(@class,'row')][" + str(i) + "]/td[1]/a").text
            if project_name == project:
                print("Project Exist")
                return True
        print("Project is None")
        return False
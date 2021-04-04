from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()



    def fill_out_group_form(self, group):
        wd = self.app.wd
        self.fill_out_group_fields("group_name", group.name)
        self.fill_out_group_fields("group_header", group.header)
        self.fill_out_group_fields("group_footer", group.footer)


    def fill_out_group_fields(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_out_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()



    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # edit group
        wd.find_element_by_name("edit").click()
        self.fill_out_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_link_text("group page")) > 0:
            return
        wd.find_element_by_link_text("group page").click()

    def count_group(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        list_groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            list_groups.append(Group(name=text, id=id))
        return list_groups
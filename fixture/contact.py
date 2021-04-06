from model.add_new_form import AddNewForm


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def fill_out_contact_form(self, add_new_form):
        wd = self.app.wd
        self.fill_out_contact_fields("firstname", add_new_form.first_name)
        self.fill_out_contact_fields("lastname", add_new_form.last_name)
        self.fill_out_contact_fields("address", add_new_form.address)
        self.fill_out_contact_fields("email", add_new_form.email)


    def fill_out_contact_fields(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def create_new_contact(self, add_new_form):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_out_contact_form(add_new_form)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()


    def edit_first_contact(self, add_new_form):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_css_selector("img[title='Edit']").click()
        self.fill_out_contact_form(add_new_form)
        wd.find_element_by_css_selector("input[value='Update']").click()
        self.return_to_home_page()


    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        list_contacts = []
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            id = element.find_element_by_name("selected[]").get_attribute("id")
            last_name = element.find_element_by_css_selector("td:nth-child(2)").text
            first_name = element.find_element_by_css_selector("td:nth-child(3)").text
            list_contacts.append(AddNewForm(last_name=last_name, first_name=first_name, id=id))
        return list_contacts


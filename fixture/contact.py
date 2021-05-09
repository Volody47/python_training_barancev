from model.add_new_form import AddNewForm
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/edit.php"):
            return
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
        self.contact_cashe = None


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cashe = None


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cashe = None


    def select_editable_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()


    def edit_first_contact(self):
        wd = self.app.wd
        self.edit_contact_by_index(0)


    def edit_contact_by_index(self, index, add_new_form):
        wd = self.app.wd
        self.open_home_page()
        self.select_editable_contact_by_index(index)
        self.fill_out_contact_form(add_new_form)
        wd.find_element_by_css_selector("input[value='Update']").click()
        self.return_to_home_page()
        self.contact_cashe = None


    def open_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_css_selector("img[title='Edit']")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_css_selector("img[title='Edit']")) > 0:
            return
        wd.find_element_by_link_text("home").click()


    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cashe = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                last_name = element.find_element_by_css_selector("td:nth-child(2)").text
                first_name = element.find_element_by_css_selector("td:nth-child(3)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text.split()
                self.contact_cashe.append(AddNewForm(last_name=last_name, first_name=first_name,
                                                     address=address, id=id, homephone=all_phones[0],
                                                     mobilephone=all_phones[1], workphone=all_phones[2],
                                                     secondaryphone=all_phones[3]))
        return list(self.contact_cashe)

    #created that method specifically for test_contact.py, in order to imlement join instead split
    def get_contact_list_version2(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cashe = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                last_name = element.find_element_by_css_selector("td:nth-child(2)").text
                first_name = element.find_element_by_css_selector("td:nth-child(3)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                all_emails = element.find_element_by_css_selector("td:nth-child(5)").text
                self.contact_cashe.append(AddNewForm(last_name=last_name, first_name=first_name,
                                                     address=address, id=id, all_emails_from_home_page=all_emails,
                                                     all_phones_from_home_page=all_phones))
        return list(self.contact_cashe)


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_editable_contact_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return AddNewForm(first_name=first_name, last_name=last_name, id=id, email=email,
                          email2=email2, email3=email3, address=address, homephone=homephone,
                          mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)


    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_css_selector("div#content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return AddNewForm(homephone=homephone, mobilephone=mobilephone,
                          workphone=workphone, secondaryphone=secondaryphone)



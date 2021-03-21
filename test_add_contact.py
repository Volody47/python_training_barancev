# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from add_new_form import AddNewForm
from application import Application

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.open_add_new_page()
        self.app.create_new_contact(AddNewForm(first_name="Vladimir", last_name="Sharapov", address="spb", email="test@gmail.com"))
        self.app.return_to_home_page()
        self.app.logout()


    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()

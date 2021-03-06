from random import randrange
import re


def test_contact_from_home_page_equel_contact_from_edit_page(app):
    list_contacts = app.contact.get_contact_list_version2()
    index = randrange(len(list_contacts))
    contact_from_home_page = app.contact.get_contact_list_version2()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.last_name == clear(contact_from_edit_page.last_name)
    assert contact_from_home_page.first_name == clear(contact_from_edit_page.first_name)
    assert contact_from_home_page.all_emails_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

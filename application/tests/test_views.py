""" This module tests all view functions  in the ShoppingList app """
import unittest
from ..views import register, login, USERS
from ..models.user import User, ItemsList


class TestViewMethods(unittest.TestCase):
    """ This class tests methods of the views module """

    def setUp(self):
        self.name = "Adri Morg"
        self.correct_username = "adri.morg"
        self.short_username = "adr"
        self.long_username = "adrianmorgangreg"
        self.invalid_chars_username = "adris@morg"
        self.correct_password = "password"
        self.short_pass = "pass"
        self.long_pass = "passwordpassword"

    def test_register_none(self):
        """ Tests the register method of the views class against various inputs """
        self.assertEqual(register(None, None, None, None), "None input")

    def test_register_blank(self):
        """ Tests the register method of the views class against blank inputs """
        self.assertEqual(register("  ", " ", "  ", " "), "Blank input")

    def test_register_username_btwn4and10(self):
        """ Tests the register method of the views class against values that lie btn 4 to 10 """
        self.assertEqual(register(self.name, self.short_username,
                                  self.correct_password, self.correct_password),
                         "Username should be 4 to 10 characters")

        self.assertEqual(register(self.name, self.long_username, self.correct_password,
                                  self.correct_password),
                         "Username should be 4 to 10 characters")

    def test_register_password_btwn6and10(self):
        """ Tests the register method of the views class against various inputs that lie between 6 to 10 """
        self.assertEqual(register(self.name, self.correct_username, self.short_pass,
                                  self.short_pass),
                         "Password should be 6 to 10 characters")
        self.assertEqual(register(self.name, self.correct_username, self.long_pass,
                                  self.long_pass),
                         "Password should be 6 to 10 characters")

    def test_register_Invalid_username(self):
        """ Tests the register method of the views class against various inputs that are invalid """
        self.assertEqual(register(self.name, self.invalid_chars_username, self.correct_password,
                                  self.correct_password),
                         "Illegal characters in username")

    def test_register_password_dontmatch(self):
        """ Tests the register method of the views class against various inputs that do not match"""
        self.assertEqual(register(self.name, self.correct_username, self.correct_password,
                                  self.long_pass),
                         "Passwords don't match")

    def test_register_successfull(self):
        """ Tests the register method of the views class against various inputs for successfull registration """
        self.assertEqual(register(self.name, self.correct_username, self.correct_password,
                                  self.correct_password),
                         "Registration successful")

    def test_login_none(self):
        """ Tests the login method of the views module for None in put """
        self.assertEqual(login(None, None), "None input")

    def test_login_blank(self):
        """ Tests the login method of the views module for blank input """
        self.assertEqual(login(" ", " "), "Blank input")

    def test_login_unknown(self):
        """ Tests the login method of the views module for unknown user """
        self.assertEqual(login("unknownuser", "unknownpass"), "User not found")
        USERS[self.correct_username] = User(self.name, self.correct_username,
                                            self.correct_password)

    def test_login_wrongpass(self):
        """ Tests the login method of the views module for wrong password """
        self.assertEqual(login(self.correct_username, "wrongpass"), "Wrong password")

    def test_login_success(self):
        """ Tests the login method of the views module for Ncorrect password """
        register(self.name, self.correct_username, self.correct_password,
                 self.correct_password)
        self.assertEqual(login(self.correct_username, self.correct_password), "Login successful")


class TestModelsMethods(unittest.TestCase):
    """ Tests methods from the various model classes in the models module """

    def setUp(self):
        self.user = User("Adri Morg", "adri.morg", "password")

    def test_add_itemsList_none(self):
        """ Tests adding a new itemsList for none input"""
        self.assertEqual(self.user.add_ItemsList(None), "None input")

    def test_add_itemsList_blank(self):
        """ Tests adding a new itemsList for nfor blank input"""
        self.assertEqual(self.user.add_ItemsList(" "), "Blank input")

    def test_add_itemsList_shortname(self):
        """ Tests adding a new itemsList for  input between 10 to 60"""
        self.assertEqual(self.user.add_ItemsList("shortname"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

    def test_add_itemsList_name_btn10and60(self):
        """ Tests adding a new itemsList for  input between 10 to 60"""

        self.assertEqual(self.user.add_ItemsList
                         ("long name long name long name long name long name long name long name"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

    def test_add_itemsList_added(self):
        """ Tests adding a new itemsList for  input added"""
        self.assertEqual(self.user.add_ItemsList("Furniture Stuff"),
                         "ItemsList added")

    def test_add_itemsList_exits(self):
        self.user.add_ItemsList("Furniture Stuff")
        self.assertEqual(self.user.add_ItemsList
                         ("Furniture Stuff"),
                         "An ItemsList with this name already exists")

    def test_update_itemsList_none(self):
        """ Tests updating a itemsList with none input"""
        self.assertEqual(self.user.update_ItemsList(None, None), "None input")

    def test_update_itemsList_blank(self):
        """ Tests updating a itemsList with blank input"""

        self.assertEqual(self.user.update_ItemsList(" ", "  "), "Blank input")

    def test_update_itemsList_not_found(self):
        """ Tests updating a itemsList for item not found"""

        self.assertEqual(self.user.update_ItemsList("notinthelistoditemsLists", "snewname"),
                         "ItemsList not found")
        self.user.add_ItemsList("Stuff stuff stuff stuff stuff")
        self.user.add_ItemsList("This is the current itemsList name")
        self.assertEqual(self.user.update_ItemsList(
            "Stuff stuff stuff stuff",
            "Stuff stuff stuff stuff"), "No change, same name")

    def test_update_itemsList_no_change(self):
        """ Tests updating a itemsList with no input change"""

        self.user.add_ItemsList("Stuff stuff stuff stuff stuff")
        self.user.add_ItemsList("This is the current itemsList name")
        self.assertEqual(self.user.update_ItemsList("This is the current itemsList name",
                                                    "Stuff stuff stuff stuff stuff"),
                         "No change, new name already in itemsList")

    def test_update_itemsList_name_btn10and60(self):
        """ Tests updating a itemsList with input between 10 and 60"""

        self.user.add_ItemsList("Stuff stuff stuff stuff stuff")
        self.user.add_ItemsList("This is the current itemsList name")

        self.assertEqual(self.user.update_ItemsList("Stuff stuff stuff stuff stuff",
                                                    "snewname"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

        self.assertEqual(self.user.update_ItemsList
                         ("Stuff stuff stuff stuff stuff",
                          "long name long name long name long name long name long name long name"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

    def test_update_itemsList_name_updated(self):
        """ Tests updating a itemsList with input updated"""

        self.user.add_ItemsList("Stuff stuff stuff stuff stuff")
        self.user.add_ItemsList("This is the current itemsList name")
        self.assertEqual(self.user.update_ItemsList("Stuff stuff stuff stuff stuff",
                                                    "stuff stuff"),
                         "ItemsList updated")

    def test_delete_itemsList(self):
        """" Test deleting a itemsList """
        self.assertEqual(self.user.delete_ItemsList(None), "None input")
        self.assertEqual(self.user.delete_ItemsList(" "), "Blank input")
        self.assertEqual(self.user.delete_ItemsList("This itemsList does not exist"), "ItemsList not found")
        self.user.add_ItemsList("Stuff stuff stuff stuff stuff")
        self.assertEqual(self.user.delete_ItemsList("Stuff stuff stuff stuff stuff"),
                         "ItemsList deleted")

    def test_add_item(self):
        """ Tests adding a new item """
        itemsList = ItemsList('Test')
        self.assertEqual(itemsList.add_item(None), "None input")
        self.assertEqual(itemsList.add_item(" "), "Blank input")
        self.assertEqual(itemsList.add_item("stuff stuff"), "Item added")
        self.assertEqual(itemsList.add_item("stuff stuff"), "Item already exists")

    def test_update_description_none(self):
        """ Tests updating item description that is a None type"""
        itemsList = ItemsList('Test')
        self.assertEqual(itemsList.update_description(None, None), "None input")

    def test_update_description_blank(self):
        """ Tests updating item description that is a blank"""

        itemsList = ItemsList('Test')
        self.assertEqual(itemsList.update_description(" ", " "), "Blank input")

    def test_update_description_no_changes(self):
        """ Tests updating item description that with no change"""

        itemsList = ItemsList('Test')
        self.assertEqual(itemsList.update_description("stuff stuff", "stuff stuff"), "No changes")

    def test_update_description_not_found(self):
        """ Tests updating item description that with item not found"""

        itemsList = ItemsList('Test')
        self.assertEqual(itemsList.update_description("stuff stuff", "stuff stuff stuff"), "Item not found")

    def test_update_newdescription(self):
        """ Tests updating item description with exitsing one"""

        itemsList = ItemsList('Test')
        itemsList.add_item("stuff stuff stuff stuff")
        itemsList.add_item("stuff stuff")
        self.assertEqual(itemsList.update_description("stuff stuff stuff stuff", "stuff stuff"),
                         "New description already in ItemsList")

    def test_update_updated(self):
        itemsList = ItemsList('Test')
        itemsList.add_item("stuff stuff stuff stuff")
        itemsList.add_item("stuff stuff")

        self.assertEqual(itemsList.update_description("stuff stuff stuff stuff", "super stuff"),
                         "Item updated")

    def test_update_status(self):
        """ Tests updating item status """
        itemsList = ItemsList('Test')
        self.assertEqual(itemsList.update_status(None, None), "None input")
        self.assertEqual(itemsList.update_status(" ", " "), "Blank input")
        self.assertEqual(itemsList.update_status("great stuff", "Pending"), "Item not found")
        itemsList.add_item("other stuff")
        itemsList.add_item("yet other stuff")
        self.assertEqual(itemsList.update_status("other stuff", "The status"), "Invalid status")
        self.assertEqual(itemsList.update_status("yet other stuff", "Done"),
                         "Item updated")

    def test_delete_item(self):
        """ Tests deleting an item from a itemsList """
        itemsList = ItemsList('Test')
        self.assertEqual(itemsList.delete_item(None), "None input")
        self.assertEqual(itemsList.delete_item(" "), "Blank input")
        self.assertEqual(itemsList.delete_item("Cool stuff"), "Item not found")
        itemsList.add_item("uncool stuff")
        self.assertEqual(itemsList.delete_item("uncool stuff"), "Item deleted")


if __name__ == '__main__':
    unittest.main()

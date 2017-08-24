import unittest
from application.models.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Adrian", "adris", "secret")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    def test_add_itemsList_None(self):
        self.assertEqual(self.user.add_ItemsList(None), "None input")

    def test_add_itemsList_blank_input(self):
        self.assertEqual(self.user.add_ItemsList(" "), "Blank input")

    def test_add_itemsList_should_be_between10and60(self):
        self.assertEqual(self.user.add_ItemsList("shortname"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

        self.assertEqual(self.user.add_ItemsList("long name long name long name long name long name long name long name"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

    def test_add_itemsList_bucket_added(self):
        self.assertEqual(self.user.add_ItemsList("Furnitures"),
                         "ItemsList added")

    def test_add_itemsList_name_already_exists(self):
        self.user.add_ItemsList("Furnitures")
        self.assertEqual(self.user.add_ItemsList
                         ("Furnitures"),
                         "An ItemsList with this name already exists")

    def test_update_ItemsList_None(self):
        self.assertEqual(self.user.update_ItemsList(None, None), "None input")

    def test_update_ItemsList_blank(self):
        self.assertEqual(self.user.update_ItemsList(" ", " "), "Blank input")

    def test_update_ItemsList_same_name(self):
        self.assertEqual(self.user.update_ItemsList("Fruits",
                                                    "Fruits"),
                         "No change, same name")

    def test_update_ItemsList_not_found(self):
        self.assertEqual(self.user.update_ItemsList("notinthelistofitemList", "snewname"),
                         "ItemsList not found")

    def test_update_ItemsList_no_change(self):
        self.user.add_ItemsList("Stationary")
        self.user.add_ItemsList("Electronics")

        self.assertEqual(self.user.update_ItemsList("Electronics",
                                                    "Stationary"),
                         "No change, new name already in itemsList")

    def test_update_ItemsList_updated(self):
        self.user.add_ItemsList("Drinks and Beer")

        self.assertEqual(self.user.update_ItemsList("Drinks and Beer",
                                                    "Clothes and Dresses"),
                         "ItemsList updated")

    def test_delete_itemsList_none(self):
        """" Test deleting a itemsList """
        self.assertEqual(self.user.delete_ItemsList(None), "None input")

    def test_delete_itemsList_blank(self):
        """" Test deleting a blank itemsList """
        self.assertEqual(self.user.delete_ItemsList(" "), "Blank input")

    def test_delete_itemsList_not_found(self):
        self.assertEqual(self.user.delete_ItemsList(
            "This itemsList does not exist"), "ItemsList not found")

    def test_delete_itemsList_deleted(self):
        self.user.add_ItemsList("This is an itemslist")
        self.assertEqual(self.user.delete_ItemsList("This is an itemslist"),
                         "ItemsList deleted")


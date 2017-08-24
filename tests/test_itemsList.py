import unittest
from application.models.shopping_list import ItemsList
class ItemListTest(unittest.TestCase):

    def setUp(self):
        self.itemsList = ItemsList("")

    def test_itemsList_instantiation(self):
        self.assertIsInstance(self.itemsList, ItemsList,
                              "Failed to instantiate")

    def test_add_item_none(self):
        self.assertEqual(self.itemsList.add_item(None), "None input")

    def test_add_item_blank(self):
        self.assertEqual(self.itemsList.add_item(" "), "Blank input")

    def test_add_item_added(self):
        self.assertEqual(self.itemsList.add_item("mangoes"), "Item added")

    def test_add_item_exists(self):
        self.itemsList.add_item("mangoes")
        self.assertEqual(self.itemsList.add_item(
            "mangoes"), "Item already exists")

    def test_update_description_none(self):
        self.assertEqual(self.itemsList.update_description(
            None, None), "None input")

    def test_update_description_blank(self):
        self.assertEqual(self.itemsList.update_description(
            " ", " "), "Blank input")

    def test_update_description_no_changes(self):
        self.assertEqual(self.itemsList.update_description(
            "Yello Mango", "Yello Mango"), "No changes")

    def test_update_description_not_found(self):
        self.assertEqual(self.itemsList.update_description(
            "Green mango", "Green Mango"), "Item not found")

    def test_update_description_exists(self):
        self.itemsList.add_item("Oranges")
        self.itemsList.add_item("Apples")
        self.assertEqual(self.itemsList.update_description("Oranges", "Apples"),
                         "New description already in ItemsList")

    def test_update_description_updated(self):
        self.itemsList.add_item("Apples")
        self.assertEqual(self.itemsList.update_description("Apples", "Berries"),
                         "Item updated")

    def test_update_status_none(self):
        self.assertEqual(self.itemsList.update_status(
            None, None), "None input")

    def test_update_status_blank(self):
        self.assertEqual(self.itemsList.update_status(" ", " "), "Blank input")

    def test_update_status_not_found(self):
        self.assertEqual(self.itemsList.update_status(
            "Stationary", "Pending"), "Item not found")

    def test_update_status_invalid(self):
        self.itemsList.add_item("Apples")
        self.itemsList.add_item("Oranges")
        self.assertEqual(self.itemsList.update_status(
            "Apples", "The status"), "Invalid status")

    # def test_update_status_item_updated(self):
    #     self.assertEqual(self.itemsList.update_status("Ream", "Done"),
    #                      "Item updated")

    def test_delete_item_none(self):

        self.assertEqual(self.itemsList.delete_item(None), "None input")

    def test_delete_item_blank(self):
        self.assertEqual(self.itemsList.delete_item(" "), "Blank input")

    def test_delete_item_not_found(self):
        self.assertEqual(self.itemsList.delete_item(
            "Laptop"), "Item not found")

    def test_delete_item(self):
        self.itemsList.add_item("Book")
        self.assertEqual(self.itemsList.delete_item("Book"), "Item deleted")

    def test_get_item_count(self):

        pass
import unittest
from application.models.item import Item

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item("")


    def test_create_item_instance(self):

        self.assertIsInstance(self.item, Item, "Failed to create instance")



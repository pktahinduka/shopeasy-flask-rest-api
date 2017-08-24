from .shopping_list import ItemsList
class User(object):
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.itemsList = {}

    def add_ItemsList(self, items_list_title):
        if items_list_title:
            if items_list_title.strip():
                if len(items_list_title) > 9 and len(items_list_title) < 61:
                    if not items_list_title in self.itemsList:
                        self.itemsList[items_list_title] = ItemsList(
                            items_list_title)
                        return "ItemsList added"
                    return "An ItemsList with this name already exists"
                return "ItemsList name should be greater than 10 and less than 60 characters"
            return "Blank input"
        return "None input"

    def update_ItemsList(self, title, new_title):
        """ Adds a new itemsList to the user's itemsLists """
        if title and new_title:
            if title.strip() and new_title.strip():
                if not title == new_title:
                    if title in self.itemsList:
                        if not new_title in self.itemsList:
                            if len(new_title) > 9 and len(new_title) < 61:
                                self.itemsList[new_title] = self.itemsList.pop(
                                    title)
                                return "ItemsList updated"
                            return (
                                "ItemsList name should be greater than 10 and less than 60 characters")
                        return "No change, new name already in itemsList"
                    return "ItemsList not found"
                return "No change, same name"
            return "Blank input"
        return "None input"

    def delete_ItemsList(self, itemsList_title):
        """ Deletes an itemslist whose name is provided from a user's itemsLists """
        if itemsList_title:
            if itemsList_title.strip():
                if itemsList_title in self.itemsList:
                    self.itemsList.pop(itemsList_title)
                    return "ItemsList deleted"
                return "ItemsList not found"
            return "Blank input"
        return "None input"


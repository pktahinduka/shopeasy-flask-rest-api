from .item import Item

class ItemsList(object):
    def __init__(self, title):
        self.title = title
        self.items = {}

    def add_item(self, description):
        """ Adds an Item to a items """
        if description:
            if description.strip():
                if not description in self.items:
                    self.items[description] = Item(description)
                    return "Item added"
                return "Item already exists"
            return "Blank input"
        return "None input"

    def update_description(self, description, new_description):
        """ Updates an Item's description in an items list """
        if description and new_description:
            if description.strip() and new_description.strip:
                if not new_description == description:
                    if not new_description in self.items:
                        if description in self.items:
                            self.items[new_description] = self.items.pop(
                                description)
                            return "Item updated"
                        return "Item not found"
                    return "New description already in ItemsList"
                return "No changes"
            return "Blank input"
        return "None input"

    def update_status(self, description, status):
        """ Updates an Item's status in a itemsList """
        if description and status:
            if description.strip() and status.strip():
                if description in self.items:
                    if status == "Pending" or status == "Done":
                        if not self.items[description].status == status:
                            self.items[description].status = status
                            return "Item updated"
                        return "Item updated"
                    return "Invalid status"
                return "Item not found"
            return "Blank input"
        return "None input"

    def delete_item(self, description):
        """ Deletes an Item from a itemslist """
        if description:
            if description.strip():
                if description in self.items:
                    self.items.pop(description)
                    return "Item deleted"
                return "Item not found"
            return "Blank input"
        return "None input"

    def get_items_count(self):
        return len(self.items)

    def get_progress(self):

        progress =0
        if self.items:
            for item in self.items.values():
                if item.status == 'Done':
                    progress = progress + 1

            return round(100*progress/len(self.items))
        return 0                
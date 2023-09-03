from flask import request, jsonify
from app.models.item_document_model import ItemDocument

class ItemDocumentController:
    def __init__(self):
        self.model = ItemDocument()

    def get_all(self):
        itemDocuments = self.model.get_all()
        return itemDocuments

    def get_by_id(self, item_id):
        ItemDocuments = self.model.get_by_id(item_id)
        if ItemDocuments:
            return ItemDocuments
        else:
            return None
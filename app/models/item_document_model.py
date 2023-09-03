from app import mongo

class ItemDocument:
    def get_all(self):
        return list(mongo.db.item_documents.find())

    def get_by_id(self, item_id):
        return mongo.db.item_documents.find({"item_id": item_id})

    # Add other methods for updating and deleting        
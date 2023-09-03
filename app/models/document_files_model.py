from app import mongo

class DocumentFiles:
    def get_all(self):
        return list(mongo.db.documents.files.find())

    def get_by_id(self, item_id):
        return mongo.db.documents.files.find({"_id": item_id})

    # Add other methods for updating and deleting        
from app import mongo

class Types:
    def get_all(self):
        return list(mongo.db.types.find())

    def get_by_id(self, type_id):
        return mongo.db.types.find({"_id": type_id})

    # Add other methods for updating and deleting        
from app import mongo

class DocumentChunks:
    def get_all(self):
        return list(mongo.db.documents.chunks.find())

    def get_by_id(self, files_id):
        return mongo.db.documents.chunks.find({"files_id": files_id})

    # Add other methods for updating and deleting        
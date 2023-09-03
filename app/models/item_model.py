from app import mongo

class Item:
    # def create_user(self, username, email):
    #     user_data = {"username": username, "email": email}
    #     mongo.db.users.insert_one(user_data)

    def create(self, data):
        return mongo.db.items.insert_one(data)

    def get_all(self):
        return list(mongo.db.items.find())

    def get_by_id(self, item_id):
        return mongo.db.items.find({"_id": item_id})
    
    def get_by_type_id(self, type_id):
        return mongo.db.items.find({"type_id": type_id})

    def get_ids_by_type_id(self, type_id):
        return mongo.db.items.find({"type_id": type_id},{"_id":1})
    
    def get_paginated_ids_by_type_id(self, type_id, skip_count, page_size):
        return mongo.db.items.find({"type_id": type_id},{"_id":1}).skip(skip_count).limit(page_size)
    
    def get_by_type_source_id(self, type_id, source_id):
        return mongo.db.items.find({"type_id": type_id,"source_id":source_id},{"_id":1})
    
    # Add other methods for updating and deleting        
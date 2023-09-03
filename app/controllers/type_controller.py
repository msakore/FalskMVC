from flask import request, jsonify
from app.models.types_model import Types
from app.controllers.item_controller import ItemController

class TypesController:
    def __init__(self):
        self.model = Types()

    def get_all(self):
        typeList = self.model.get_all()
        return typeList

    def get_by_id(self,type_id):
        type = self.model.get_by_id(type_id)
        if type:
            return type
        else:
            return None
        

    # this function to be continue for files migration by catagory
    def convert_paginated_file_of_catagory_by_id(self,cat_id, page_id):
        type = list(self.model.get_by_id(cat_id))

        if type:
            itemObj = ItemController()
            typeItemIdList = itemObj.get_paginated_ids_by_type_id(cat_id, page_id)


            return jsonify({"typeDetails": typeItemIdList})
        else:
            return jsonify({"message": "Type not found"}), 404
        

    # this function to be continue for data migration by catagory      
    def migrate_by_catagory_id(self, cat_id):        
        type = list(self.model.get_by_id(cat_id))
        if type:
            itemObj = ItemController()
            typeItemList = itemObj.get_by_type_id(cat_id)


            return jsonify({"typeDetails": typeItemList})
        else:
            return jsonify({"message": "Type not found"}), 404
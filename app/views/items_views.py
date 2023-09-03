from flask import Blueprint
from app.controllers.item_controller import ItemController
from app.controllers.type_controller import TypesController

item_bp = Blueprint("items", __name__)
item_controller = ItemController()
type_controller = TypesController()

# @item_bp.route("/items", methods=["GET"])
# def get_all_items():
#     return item_controller.get_all()

@item_bp.route("/items/<string:item_id>", methods=["GET"])
def get_items_by_id(item_id):
    return item_controller.get_by_id_jsonify(item_id)




#----------------------------converion routes--------------------------#

@item_bp.route("/convert/item/<string:item_id>", methods=["GET"])
def convert_file_of_items_by_id(item_id):
    return item_controller.convert_file_of_items_by_id(item_id)

@item_bp.route("/convert/catagory/<string:cat_id>", methods=["GET"]) #to be continued
def convert_file_of_catagory_by_id(cat_id):
    return type_controller.convert_file_of_catagory_by_id(cat_id)

@item_bp.route("/convert/catagory/paginate/<string:cat_id>/<int:page_id>", methods=["GET"]) #to be continued
def convert_paginated_file_of_catagory_by_id(cat_id, page_id):
    return type_controller.convert_paginated_file_of_catagory_by_id(cat_id, page_id)


convert_paginated_file_of_catagory_by_id
 



#---------------------------Migration Route---------------------------#

@item_bp.route("/migrate/org/<string:src_id>", methods=["GET"]) #to be continued
def migrate_org_by_source_id(src_id):
    return item_controller.migrate_org_by_source_id(src_id)
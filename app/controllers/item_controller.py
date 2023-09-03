import os
import requests
from flask import request, jsonify
from app.models.item_model import Item
from app.utils.s3_utility import S3Utility
from app.controllers.item_document_controller import ItemDocumentController
from app.controllers.document_files_controller import DocumentFilesController
from app.controllers.document_chunks_controller import DocumentChunksController

class ItemController:
    def __init__(self):
        self.model = Item()

    # def create_user():
    #     data = request.get_json()
    #     username = data.get('username')
    #     email = data.get('email')
    #     Item().create_user(username, email)
    #     return jsonify({"message": "User created successfully"}), 201

    # def create(self):
    #     data = request.get_json()
    #     result = self.model.create(data)
    #     return jsonify({"message": "Todo created successfully", "id": str(result.inserted_id)})

    def get_all(self):
        items = self.model.get_all()
        return jsonify({"items": items})
    

    def get_by_id_jsonify(self, item_id):
        item = self.model.get_by_id(item_id)
        if item:
            return jsonify({"item": item})
        else:
            return jsonify({"message": "item not found"}), 404
        
        
    def get_by_id(self, item_id):
        item = list(self.model.get_by_id(item_id))
        if item:
            return item
        else:
            return None
    
        
    def get_by_type_id(self, type_id):
        itemList = list(self.model.get_by_type_id(type_id))
        if itemList:
            return itemList
        else:
            return None
        
    
    def get_paginated_ids_by_type_id(self, type_id, page = 1, page_size = 5):
        skip_count = (page - 1) * page_size
        itemList = list(self.model.get_paginated_ids_by_type_id(type_id, skip_count, page_size))
        if itemList:
            return itemList
        else:
            return None
        
        
    def get_by_type_source_id(self, type_id, source_id):
        itemList = list(self.model.get_by_type_source_id(type_id, source_id))
        if itemList:
            return itemList
        else:
            return None
    
    def convert_file_of_items_by_id(self, item_id):
        item = self.model.get_by_id(item_id)
        
        if item:
            itemDocumentObj = ItemDocumentController()
            ItemDocuments = itemDocumentObj.get_by_id(item_id)
            ItemDocuments = list(ItemDocuments)
            if not ItemDocuments:
                return jsonify({"message": "item documetns not found"}), 404
            else:
                documentId = ItemDocuments[0]['document_id']
                #documentFiles
                documentFileObj = DocumentFilesController()
                documentFiles = documentFileObj.get_by_id(documentId)
                documentFiles = list(documentFiles)
                contentType = documentFiles[0]['contentType']
                fileName = documentFiles[0]['filename']
                #documentChunks
                documentChunkObj = DocumentChunksController()
                documentChunks = documentChunkObj.get_by_id(documentId)
                documentChunks = list(documentChunks)
                for documentChunk in documentChunks:
                    if 'byte_data' in locals() or 'byte_data' in globals():
                        byte_data += documentChunk['data']
                    else:
                        byte_data = documentChunk['data']

                mime_type = contentType

                # Generate a unique file name
                file_name = f"{fileName}"

                script_directory = os.path.dirname(os.path.abspath(__file__))
                script_directory = script_directory.replace("app\controllers", "files")

                output_pdf_path = os.path.join(script_directory, file_name)

                # # Write the byte data to a new file
                with open(output_pdf_path, "wb") as file:
                    file.write(byte_data)
                
                s3 = S3Utility()
                if s3.upload_file(output_pdf_path, file_name):
                    print('File uploaded successfully')
                else:
                    print('File upload failed')

                # return f"File '{file_name}' successfully created."
                return jsonify({"fileName": output_pdf_path,"mimeType": mime_type})
        else:
            return jsonify({"message": "item not found"}), 404
        

    def finalise_item_obj(self, itemDetails):
        itemObj                             = {}
        itemObj['address']                  = {}
        itemObj['website']                  = {}
        itemObj['id']                       = itemDetails['_id']
        itemObj['name']                     = itemDetails['name']
        itemObj['status']                   = itemDetails['structure']['organization_approval_status']
        itemObj['createdOn']                = itemDetails['created'].strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        itemObj['entityType']               = 'Organization'
        itemObj['description']              = itemDetails['structure']['organization_desc']
        itemObj['activeStatus']             = itemDetails['structure']['organization_active_status']
        itemObj['nameLowerCase']            = itemDetails['name'].lower()
        itemObj['lastModifiedOn']           = itemDetails['modified'].strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        itemObj['isMigratedData']           = True
        itemObj['address']['zip']           = itemDetails['structure']['zip']
        itemObj['address']['city']          = itemDetails['structure']['city']
        itemObj['address']['county']        = itemDetails['structure']['county']
        itemObj['address']['country']       = itemDetails['structure']['country']
        itemObj['address']['address1']      = itemDetails['structure']['address_1']
        itemObj['address']['address2']      = itemDetails['structure']['address_2']
        itemObj['address']['latitude']      = itemDetails['structure']['latitude']
        itemObj['address']['longitude']     = itemDetails['structure']['longitude']
        itemObj['website']['websiteLink']   = itemDetails['structure']['website']

        return itemObj
    

    def send_data_to_api(self, api_url):
        api_url = 'https://api.example.com/data'  # Replace with the API endpoint you want to call

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                # API call was successful, return the data as JSON
                data = response.json()
                return jsonify(data)
            else:
                # Handle API errors
                return jsonify({'error': 'API call failed'}), response.status_code
        except Exception as e:
            # Handle other exceptions like network errors
            return jsonify({'error': str(e)}), 500
        
        
    def migrate_org_by_source_id(self, source_id):    
            cat_id = "6F3A9C3075C711E684EB00155D031225"
            source_id = "45E92B8296B107ACE05332091E0A22F1" #splc
            typeItemIdList = self.get_by_type_source_id(cat_id,source_id)

            i = 1
            for item in typeItemIdList:
                itemDetails = self.get_by_id(item['_id'])
                print(itemDetails)
                itemObj = self.finalise_item_obj(itemDetails[0])


                break
            return jsonify({"typeDetails": itemObj})
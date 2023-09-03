from flask import request, jsonify
from app.models.document_files_model import DocumentFiles

class DocumentFilesController:
    def __init__(self):
        self.model = DocumentFiles()

    def get_all(self):
        documentFiles = self.model.get_all()
        return jsonify({"DocumentFiles": documentFiles})

    def get_by_id(self, document_id):
        DocumentFile = self.model.get_by_id(document_id)
        if DocumentFile:
            return DocumentFile
        else:
            return None
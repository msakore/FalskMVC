from flask import request, jsonify
from app.models.document_chunks_model import DocumentChunks

class DocumentChunksController:
    def __init__(self):
        self.model = DocumentChunks()

    def get_all(self):
        DocumentChunks = self.model.get_all()
        return jsonify({"DocumentChunks": DocumentChunks})

    def get_by_id(self, files_id):
        DocumentChunk = self.model.get_by_id(files_id)
        if DocumentChunk:
            return DocumentChunk
        else:
            return None
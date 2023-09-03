import os
import boto3
from botocore.exceptions import NoCredentialsError

class S3Utility:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket_name = os.environ.get('AWS_S3_BUCKET_NAME')
        self.bucket_directory = os.environ.get('AWS_S3_DIRECTORY')

    def upload_file(self, file_name, object_name):
        try:
            object_name = self.bucket_directory + object_name
            self.s3.upload_file(file_name, self.bucket_name, object_name)
            return True
        except FileNotFoundError:
            return False
        except NoCredentialsError:
            return False

    def download_file(self, object_name, file_name):
        try:
            self.s3.download_file(self.bucket_name, object_name, file_name)
            return True
        except FileNotFoundError:
            return False
        except NoCredentialsError:
            return False

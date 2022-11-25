import os
from pprint import pprint
from google.cloud import storage

credentials_path = 'Project/asesoriasonline-ead83ac573f6.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

storage_client = storage.Client()

bucket_name =  'bucket-docs-ing-software'

"""
Get Bucket
"""
my_bucket = storage_client.get_bucket(bucket_name)
print(vars(my_bucket))

"""
Upload File
"""
def upload_to_bucket(blob_name, file_path, bucket_name):
    '''
    Upload file to a bucket
    : blob_name  (str) - object name
    : file_path (str)
    : bucket_name (str)
    '''
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob




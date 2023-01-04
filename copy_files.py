import os
from dotenv import load_dotenv
load_dotenv('.env')
from azure.storage.blob import BlockBlobService


def upload_directory_to_azure(path,directory_name, container_name):
    try:
        account_name =  os.environ.get("STORAGE_ACCOUNT_NAME")
        account_key = os.environ.get("STORAGE_ACCOUNT_KEY")
        block_blob_service = BlockBlobService(account_name, account_key)
        path_remove = path
        local_path = path+directory_name

        for r,d,f in os.walk(local_path):        
            if f:
                for file in f:
                    file_path_on_azure = os.path.join(r,file).replace(path_remove,"")
                    file_path_on_local = os.path.join(r,file)
                    block_blob_service.create_blob_from_path(container_name,file_path_on_azure,file_path_on_local) 
                    print("File uploaded to Azure: ",file_path_on_azure)
            
        print("Directory uploaded to Azure: ",directory_name)
        print("upload complete")
    except Exception as e:
        print(e)           

if __name__ == "__main__":
    upload_directory_to_azure("C:/Users/nostr/Downloads/","stocks_data",os.environ.get("CONTAINER_NAME"))



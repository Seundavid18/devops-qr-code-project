from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import qrcode
from azure.storage.blob import BlobServiceClient, ContentSettings
import os
from io import BytesIO

# Loading Environment variable (AWS Access Key and Secret Key)
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Allowing CORS for local testing
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Azure storage configuration

# Set Azure Storage account credentials from environment variables
azure_storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
azure_storage_account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")

# Build the connection string
connection_string = f"DefaultEndpointsProtocol=https;AccountName={azure_storage_account_name};AccountKey={azure_storage_account_key};EndpointSuffix=core.windows.net"

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Specify the container name
container_name = 'qrcode-storage'  


@app.post("/generate-qr/")
async def generate_qr(url: str):
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR Code to BytesIO object
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Upload to Azure Blob Storage
    response = upload_to_blob_storage(img_byte_arr, url)

    return response


def upload_to_blob_storage(img_byte_arr, url):
    # Generate file name for Az storage
    file_name = f"qr_codes/{url.split('//')[-1]}.png"

    try:
        # Ensure the container exists
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()

        # Upload the blob (file)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        blob_client.upload_blob(img_byte_arr, blob_type="BlockBlob", overwrite=True, content_settings=ContentSettings(content_type='image/png'))

        # Generate the Blob URL
        azure_blob_url  = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{file_name}"
        return { "qr_code_url": azure_blob_url }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        
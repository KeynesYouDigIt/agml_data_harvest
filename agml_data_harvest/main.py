from fastapi import Body, FastAPI, Form, File, UploadFile, Request
from agml_data_harvest.models import DatasetMetadata

import json

app = FastAPI()

UPLOAD_PATH = "/upload_new_dataset"
DOWNLOAD_PATH = "/download_dataset"  # and some arg...

@app.get("/")
async def welcome_and_go_to_docs(request: Request):
    docs_url = f"{request.client.host}/docs"
    return {"message": f"Welcome to AGML's data harvester! please head to {docs_url}"}

@app.post(UPLOAD_PATH)
async def upload_new_dataset(metadata: str = Form(...), file: UploadFile = File(...)):
    """
    Upload an image file along with its metadata.

    The metadata should be a JSON object that matches the ImageMetadata model.
    The file should be an image file. The contents of the file will be logged and can be processed as needed.
    
    
    curl -X POST "http://yourdomain.com/upload_path" \
     -H "Content-Type: multipart/form-data" \
     -F "metadata={"name": "myset", "description": "such a nice data set};type=application/json \
     -F "file=@/path/to/your/file.ext"
    """
    # Process binary data
    parsed_metadata = DatasetMetadata.parse_raw(metadata)
    contents = await file.read()
    
    # Log the metadata and binary data
    print(f"Metadata: {parsed_metadata}")
    print(f"Binary Data: {contents}")

    return {"filename": file.filename}

app.get(DOWNLOAD_PATH)
def download_dataset():
    return {"message": "IMMA DOWNLIDING MY DATA SET....... jk not implemented."}
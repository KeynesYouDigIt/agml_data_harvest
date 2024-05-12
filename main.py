from fastapi import Body, FastAPI, Form, File, UploadFile
from .models import DatasetMetadata

import json

app = FastAPI()


@app.post("/upload_new_dataset")
async def uplead_new_dataset(metadata: DatasetMetadata = Body(...), file: UploadFile = File(...)):
    """
    Upload an image file along with its metadata.

    The metadata should be a JSON object that matches the ImageMetadata model.
    The file should be an image file. The contents of the file will be logged and can be processed as needed.
    """
    # Process binary data
    contents = await file.read()
    
    # Log the metadata and binary data
    print(f"Metadata: {metadata}")
    print(f"Binary Data: {contents}")
    
    return {"filename": file.filename}
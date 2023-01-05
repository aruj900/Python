from fastapi import FastAPI,UploadFile,File
import secrets
from fastapi.staticfiles import StaticFiles
from PIL import Image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"),name='static')

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile= File(...)):
    FILEPATH = "./static/images"
    filename = file.filename
    extention = filename.split(".")[1]
    token_name = secrets.token_hex(10) + "." + extention
    generated_name = FILEPATH + token_name
    file_content = await file.read()
    with open(generated_name, "wb") as file:
        file.write(file_content)
    file.close()
    file_url = "127.0.0.1:8000" + generated_name[1:] #save this to databases
    
    return {"filename": filename}



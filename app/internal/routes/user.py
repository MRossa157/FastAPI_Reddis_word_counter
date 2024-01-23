import os
from datetime import datetime

from fastapi import APIRouter
from fastapi import File, UploadFile

router = APIRouter(
    prefix='/api/v1'
)

@router.get('/hello')
def user_hello():
    return {'hello': 'world'}

#TODO: Добавить построчную отправку в топик брокера RabbitMQ
@router.post('/load')
def upload(file: UploadFile = File(...)):
    try:
        os.mkdir("images")
        print(os.getcwd())
    except Exception as e:
        print(e)
        
    file_name = os.getcwd()+"/images/"+file.filename.replace(" ", "-")
    
    try:
        contents = file.file.read()
        with open(file_name, 'wb') as f:
            f.write(contents)
    except Exception:
        return {
            "datetime": f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S.%f')[:-3]}",
            "title": None,
            "text": None,
            "status": "error",
            "message": "There was an error uploading the file"
        }
    finally:
        file.file.close()
    # return {
    #         "datetime": f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S.%f')[:-3]}",
    #         "title": None,
    #         "text": None,
    #     } 
        
    
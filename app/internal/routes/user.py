import os
from datetime import datetime

from app.pkg.redds_tools.tools import RedisTools

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
        book_bytes = file.file.read()
    except Exception:
        return {
            "datetime": f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S.%f')[:-3]}",
            "title": None,
            "text": None,
            "error": "There was an error uploading the file"
        }
    finally:
        file.file.close()
    
    book_text = book_bytes.decode("utf-8")
    book_title = file.filename
    
    RedisTools.set_data(book_title, book_text)
    
    return {
            "datetime": f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S.%f')[:-3]}",
            "title": book_title,
            "text": book_text,
        }
        
    
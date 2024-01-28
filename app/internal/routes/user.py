from datetime import datetime

from app.pkg.redds_tools.tools import RedisTools

from fastapi import APIRouter
from fastapi import File, UploadFile

router = APIRouter(
    prefix='/api/v1'
)

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
    
    lines = book_text.split('\n')
    total_lines = len(lines)
    total_x_count = sum(line.count('Х') for line in lines)
    
    x_avg_count_in_line = round(total_x_count / total_lines if total_lines > 0 else 0, 3)
    
    time = f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S.%f')[:-3]}"
    
    RedisTools.set_file_data(book_title, [time, book_title, x_avg_count_in_line])
    
    return {
            "datetime": time,
            "title": book_title,
            "x_avg_count_in_line": x_avg_count_in_line,
        }
    
    
        
@router.get('/files')
def get_all_data():
    all_data = []
    for key in RedisTools.get_keys():
        data = RedisTools.get_data(key)
        all_data.append({"datetime": data[0], "title": data[1], "x_avg_count_in_line": data[2]})

    return all_data
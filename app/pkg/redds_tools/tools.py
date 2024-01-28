import redis
from typing import Tuple

class RedisTools:
    
    __redis_connect = redis.Redis(host='redis', port=6379)
    
    @classmethod
    def set_file_data(cls, title: str, data: Tuple[str, str, float]):
        '''
        Метод для добавления данных о файле в Rabit
        Пример
        title: str = 'Хорошая книга'
        data = [timestamp, book_title, x_avg_count_in_line]
        '''
        cls.__redis_connect.rpush(title, *data)
        
    @classmethod
    def get_data(cls, key):
        return cls.__redis_connect.lrange(key, 0, -1)
    
    @classmethod
    def get_keys(cls):
        return cls.__redis_connect.keys(pattern='*')
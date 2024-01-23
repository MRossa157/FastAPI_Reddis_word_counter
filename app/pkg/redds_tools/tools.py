import redis

class RedisTools:
    
    __redis_connect = redis.Redis(host='redis', port=6379)
    
    @classmethod
    def set_data(cls, title: str, x_avg_count_in_line: float):
        cls.__redis_connect.set(title, x_avg_count_in_line)
        
    @classmethod
    def get_data(cls, title):
        return cls.__redis_connect.get(title)
    
    @classmethod
    def get_keys(cls):
        return cls.__redis_connect.keys(pattern='*')
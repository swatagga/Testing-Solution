import psycopg2
import redis
from psycopg2.extras import RealDictCursor

cache = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_query(query_key):
    cached_data = cache.get(query_key)
    if cached_data:
        return cached_data.decode("utf-8")
    return None

def set_cached_query(query_key, data, expiration=300):
    cache.set(query_key, data, ex=expiration)  # Cache results for 5 minutes
    
# Add retrieval method

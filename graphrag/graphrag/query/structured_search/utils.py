# utils.py
import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def log_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        logger.info(f'Function {func.__name__} took {total_time:.4f} seconds')
        return result
    return wrapper
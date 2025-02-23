import time

def timing_counter(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(2)
        result = function(*args, **kwargs)
        end = time.time()
        print(f"A la función {function.__name__} le tomó {end-start:.5f} segundos realizar su proceso.")
        return result
    return wrapper
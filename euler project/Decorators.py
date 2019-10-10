from functools import wraps




def timer(func):
    import time
    @wraps(func)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time() - t1
        print('{} function executed in {}'.format(func.__name__,t2))
        return result
    return wrapper


def logger():
    import logging
    logging.basicConfig(filename="{}.log".format(func.__name__),level=logging.INFO)
    @wraps(func)
    
    def wrapper(*args,**kwargs):
        logging.info("{} func done with args: {} and kwargs:{}".format(
            func.__name__,args,kwargs))
        return func(*args,**kwargs)
    return wrapper

# logs func if file name not given then logging into doc with the same name 
# as func else with your given
def custom_logger(file_name=''):        
    def decorator(func):
        import logging
        logging.basicConfig(filename="{}.log".format
                            (func.__name__ if not file_name else file_name)
                            ,level=logging.INFO)
        @wraps(func)
        def wrapper(*args,**kwargs):
            logging.info("{} func done with args: {} and kwargs:{}".format(
            func.__name__,args,kwargs))
            return func(*args,**kwargs)
        return wrapper
    return decorator



#@timer
#@custom_logger()
#def arr_creater(ii,jj):
#    arr = []
#    for i in range(ii):
#        arr.append([])
#        for j in range(jj):
#            arr[i].append(j)
#    return arr


#arr_creater(1000,10000)

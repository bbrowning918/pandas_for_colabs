import cProfile, pstats, io
from functools import wraps
from time import time

def profile(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        profiler = cProfile.Profile()
        result = profiler.runcall(f, *args, **kwargs)
        
        s = io.StringIO()
        pstats.Stats(profiler, stream=s).sort_stats('cumulative').print_stats()

        print(F"{f.__name__}@{len(args[0])}")
        print(s.getvalue())
        print("_" * 10)

        return result
    return wrap

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()

        print(F"{f.__name__}@{len(args[0])}")
        print(F"time: {end-start:2.4f} s - profiler can't see inside :(")
        
        return result
    return wrap

import cProfile, pstats, io
from functools import wraps

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


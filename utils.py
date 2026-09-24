import time
from functools import wraps

def retry(times=3, delay=1.0):
    def deco(fn):
        @wraps(fn)
        def wrap(*a, **kw):
            for i in range(times):
                try:
                    return fn(*a, **kw)
                except Exception:
                    if i == times - 1:
                        raise
                    time.sleep(delay)
        return wrap
    return deco

def batches(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]

#!/usr/bin/env python
import functools
import logging

# Configure logging.
# See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
def config_logger(logger):
    logger.setLevel(logging.WARNING)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def add_logger(f):
    """(Decorator) Add a logger to a function
    
    Within the new function, `logger` refers to a Logger object
    with a qualified name like "module.function" or "module.class.method".

    Decorators are the most pythonic way to get the name of a function
    seemingly from within that function.
    See https://stackoverflow.com/a/33162541/297797

    CAUTION: Since python is lexically scoped, this hack reassigns
    a global variable.  See https://stackoverflow.com/q/17862185/297797

    """
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        globs = f.__globals__
        sentinel = object()
        logger_o = globs.get('logger',sentinel)
        globs['logger'] = logging.getLogger(f.__module__).getChild(f.__qualname__)
        try:
            result = f(*args, **kwargs)
        finally:
            if logger_o is sentinel:
                del globs['logger']
            else:
                globs['logger'] = logger_o
        return result
    wrapped.__name__ = f.__name__
    wrapped.__doc__ = f.__doc__
    return wrapped


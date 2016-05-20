

import random
from flask import Flask
from flask_cache import Cache


app = Flask(__name__)
cache = Cache(app=app, config={'CACHE_TYPE': 'simple'})


# With functions that do not receive arguments, cached() and memoize() are effectively the same.

@app.route('/')
@cache.cached(timeout=10)   # same as cache.memoize(timeout=10)
def cached():
    r = random.randint(-1024, 1024)
    return "<h1> %s </h1>" % r


@app.route('/<int:a>/<int:b>')
@cache.memoize(timeout=16)
def cache_memoize(a, b):       # In memoization, the functions arguments (a and b) are also included into the cache_key.
    ran = random.randint(0, 10000)
    return "</h1> %s + %s + %s = %s </h1>" % (a, b, ran, a+b+ran)


if __name__ == '__main__':
  app.run()

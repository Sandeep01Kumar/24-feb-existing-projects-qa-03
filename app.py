"""Flask application that serves as a Backprop integration test fixture.

A minimal HTTP server that responds to every request with a plain-text
'Hello, World!' greeting. This is the Python 3 / Flask equivalent of the
original Node.js server.js implementation.
"""

from flask import Flask, make_response

HOST = '127.0.0.1'
PORT = 3000

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=[
    'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD',
])
@app.route('/<path:path>', methods=[
    'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD',
])
def hello(path):
    """Handle every HTTP request with an identical plain-text response.

    This handler ignores the request method, path, headers, and body —
    mirroring the deterministic, stateless behavior of the original Node.js
    server. Every request receives a 200 OK response with Content-Type
    text/plain and body 'Hello, World!\n'.

    Args:
        path: The URL path segment captured by the catch-all route.
              Accepted but intentionally unused.

    Returns:
        A Flask Response object with status 200, Content-Type text/plain,
        and body 'Hello, World!\n'.
    """
    response = make_response('Hello, World!\n', 200)
    response.headers['Content-Type'] = 'text/plain'
    return response


if __name__ == '__main__':
    print(f'Server running at http://{HOST}:{PORT}/')
    app.run(host=HOST, port=PORT)

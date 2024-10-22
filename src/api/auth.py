from functools import wraps
from flask import request, jsonify

API_KEY = 'your-secure-api-key'

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if api_key and api_key == API_KEY:
            return f(*args, **kwargs)
        else:
            return jsonify({'message': 'Unauthorized'}), 401
    return decorated_function

# Usage example:
# @app.route('/some-endpoint')
# @require_api_key
# def some_endpoint():

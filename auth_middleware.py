from flask import g, request, jsonify
from functools import wraps
import jwt
import os

def auth_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
       
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({'error': 'No authorization header'}), 401
        
        try:
            token = auth_header.split(' ')[1]
        except IndexError:
            return jsonify({'error': 'Invalid authorization header format'}), 401
        
       
        try:
            secret_key = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            
            
            g.user_id = payload.get('user_id')
            g.user_email = payload.get('email')
            g.user_role = payload.get('role', 'user')
            
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        
        return f(*args, **kwargs)
    
    return decorated_function

def admin_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({'error': 'No authorization header'}), 401
        
        try:
            token = auth_header.split(' ')[1]
        except IndexError:
            return jsonify({'error': 'Invalid authorization header format'}), 401
        
        
        try:
            secret_key = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            
            
            g.user_id = payload.get('user_id')
            g.user_email = payload.get('email')
            g.user_role = payload.get('role', 'user')
            
            
            if g.user_role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        
        return f(*args, **kwargs)
    
    return decorated_function

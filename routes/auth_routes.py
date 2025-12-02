from flask import Blueprint, request
from database import get_db
import bcrypt
import jwt
from datetime import datetime, timedelta
import os

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    json_data = request.get_json()
    
    # TODO: Implement login logic
    
    pass


@auth_bp.route("/register", methods=["POST"])
def register():
    json_data = request.get_json()
    
    # TODO: Implement register logic
    
    pass

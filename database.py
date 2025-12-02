from flask import g
import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_db():
    """
    Get a database connection. If one doesn't exist in the Flask g object,
    create a new connection and store it.
    
    Returns:
        psycopg2.connection: Database connection object
    """
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("Connected to postgres")
    return g.db

def close_db(e=None):
    """
    Close the database connection if it exists.
    This should be called at the end of each request.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

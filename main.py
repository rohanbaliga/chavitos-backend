from flask import Flask, g
from database import get_db, close_db
from auth_middleware import auth_middleware
from routes.auth_routes import auth_bp
from routes.queue_routes import queue_bp
from routes.appointment_routes import appointment_bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(queue_bp)
app.register_blueprint(appointment_bp)

app.teardown_appcontext(close_db)


@app.route('/test', methods=['GET'])
@auth_middleware
def test():
    # TODO: Implement test endpoint to verify auth middleware
    pass


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

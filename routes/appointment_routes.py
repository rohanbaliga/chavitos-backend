from flask import Blueprint, request, g
from database import get_db
from auth_middleware import auth_middleware, admin_middleware

appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointment')

@appointment_bp.route("/create", methods=["POST"])
@auth_middleware
def create_appointment():
    username = g.username
    json_data = request.get_json()
    
    # TODO: Implement create appointment logic
    
    pass


@appointment_bp.route("/read", methods=["GET"])
@auth_middleware
def read_appointments():
    username = g.username
    
    # TODO: Implement read appointments logic
    
    pass


@appointment_bp.route("/delete/<int:appointment_id>", methods=["DELETE"])
@auth_middleware
def delete_appointment(appointment_id):
    username = g.username
    
    # TODO: Implement delete appointment logic
    
    pass


@appointment_bp.route("/admin/read", methods=["GET"])
@auth_middleware
@admin_middleware
def admin_read_appointments():
    
    # TODO: Implement admin read appointments logic
    
    pass


@appointment_bp.route("/admin/edit/<int:appointment_id>", methods=["PUT"])
@auth_middleware
@admin_middleware
def admin_edit_appointment(appointment_id):
    json_data = request.get_json()
    
    # TODO: Implement admin edit appointment logic
    
    pass


@appointment_bp.route("/admin/delete/<int:appointment_id>", methods=["DELETE"])
@auth_middleware
@admin_middleware
def admin_delete_appointment(appointment_id):
    
    # TODO: Implement admin delete appointment logic
    
    pass

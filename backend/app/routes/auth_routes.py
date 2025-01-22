from flask import Blueprint, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Itt kezelheted a bejelentkezést
    return jsonify({"message": "Login endpoint"})

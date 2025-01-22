from flask import Flask
from flask_cors import CORS
from .routes.api_routes import api_bp
from .routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    CORS(app, origins=["http://localhost:5029"])

    # Regisztrálj minden Blueprint-et
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

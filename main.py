from flask import Flask, Blueprint, render_template
from .auth import auth as auth_bp  # Correct relative import

# Create a Blueprint named 'main'
main_bp = Blueprint('main', __name__)

# Define routes within the 'main' Blueprint
@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/profile')
def profile():
    return "Profile here"

@main_bp.route('/login')
def login():
    return render_template('login.html')

# Create the Flask application instance using the application factory pattern
def create_app():
    app = Flask(__name__, static_folder='static')

    # Register the 'main' Blueprint with the Flask application
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)  # Register the correct blueprint

    return app

# Ensure that 'app' is created using the factory function when this script is executed
app = create_app()

# Only run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)

# Load configuration
app.config.from_object('config.Config')

# Initialize database (we won’t use this yet, keeping everything in memory)
db = SQLAlchemy(app)

# Import and register the routes from routes.py
from app.routes import app_routes
app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run(debug=True)

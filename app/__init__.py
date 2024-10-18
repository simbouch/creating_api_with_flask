from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)

# Load configuration
app.config.from_object('config.Config')

# Initialize database
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)

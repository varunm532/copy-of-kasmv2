# init_db.py

from __init__ import app, db
from model.user import initUsers

# Ensure the app context is available
with app.app_context():
    # Create all tables
    db.create_all()
    # Initialize the Users table
    initUsers()
    print("Database initialized!")

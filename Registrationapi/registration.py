from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registration.db'  # SQLite database file
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    gender = db.Column(db.String(10))

    def __init__(self, first_name, last_name, email, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender

# Initialize the database and create the User table
with app.app_context():
    db.create_all()

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if all required fields are present
    required_fields = ['first_name', 'last_name', 'email', 'gender', 'password', 'confirm_password']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Check if email is in the correct format
    if '@' not in data['email']:
        return jsonify({'error': 'Invalid email format'}), 400

    # Check if passwords match
    if data['password'] != data['confirm_password']:
        return jsonify({'error': 'Passwords do not match'}), 400

    # Save the user data to the database
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        gender=data['gender']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': f'Registration successful, Welcome {data["first_name"]}'}), 200

if __name__ == '__main__':
    app.run(debug=True)

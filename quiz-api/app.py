# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from database import create_question, get_all_questions  
# from question import db
from flask import Flask, request
from jwt_utils import build_token, decode_token
import hashlib

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for SQLAlchemy

# Initialize the database
# db.init_app(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/questions', methods=['POST'])
def post_question():
    token = request.headers.get('Authorization')

    question_data = request.get_json()

    question_result = create_question(token, question_data)

    return jsonify(question_result), 201 

@app.route('/questions', methods=['GET'])
def get_all_questions_route():
    try:
        # Call the new function to get all questions
        questions = get_all_questions()

        # Convert the list of questions to a serialized format
        serialized_questions = [question.to_dict() for question in questions]

        return jsonify(serialized_questions), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def postLogin():
	payload = request.get_json()
	tried_password = payload['password'].encode('UTF-8')
	hashed = hashlib.md5(tried_password).digest()

	if hashed == b'AM\x179\\G\xd5\xd2`$\xfc\xaf\x9d\x82z\\':
		access_token = build_token() 
		return {'token':access_token}, 200
	else:
		return 'Unauthorized', 401


if __name__ == "__main__":
    app.run()


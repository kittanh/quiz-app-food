from flask import Flask, request, jsonify
from flask_cors import CORS
<<<<<<< HEAD
from database import save_question, db
# from question import db
=======
from flask import Flask, request
from jwt_utils import build_token, decode_token
import hashlib
>>>>>>> 2d18ca9c2aae65ea750f9da7300656d141a34f58

app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'  # SQLite database file
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for SQLAlchemy

# # Initialize the database
# db.init_app(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

<<<<<<< HEAD

@app.route('/api/questions', methods=['POST'])
def post_question():
    token = request.headers.get('Authorization')

    question_data = request.get_json()

    question_result = save_question(token, question_data)

    return jsonify(question_result), 201 
=======
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

>>>>>>> 2d18ca9c2aae65ea750f9da7300656d141a34f58


if __name__ == "__main__":
    app.run()


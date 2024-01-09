from flask import Flask, request, jsonify
from flask_cors import CORS
from database import save_question, db
# from question import db

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


@app.route('/api/questions', methods=['POST'])
def post_question():
    token = request.headers.get('Authorization')

    question_data = request.get_json()

    question_result = save_question(token, question_data)

    return jsonify(question_result), 201 


if __name__ == "__main__":
    app.run()
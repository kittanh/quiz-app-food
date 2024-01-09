from flask import Flask
from flask_cors import CORS
from flask import Flask, request
from jwt_utils import build_token, decode_token
import hashlib

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

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


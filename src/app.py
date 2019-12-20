import os

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/hello', methods=['GET'])
def hello():

    return jsonify({"message": "Hello World!"}), 200

@app.route('/favicon.ico')
def favicon():

    return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
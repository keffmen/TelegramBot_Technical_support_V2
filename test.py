from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


@app.route('/upload', methods=['POST'])
def webhook():
    print(request.form.get('name'))
    return jsonify({'status': '200'}), 200


if __name__ == '__main__':
    app.run(port=8081)

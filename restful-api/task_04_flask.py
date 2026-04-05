#!/usr/bin/python3
"""
Flask modulu ilə sadə RESTful API-nin qurulması.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}


@app.route('/')
def home():
    """Ana səhifə üçün endpoint"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Sistemdəki bütün istifadəçi adlarının siyahısını qaytarır"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """API-nin vəziyyətini yoxlamaq üçün endpoint"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Verilmiş istifadəçi adına görə məlumatları qaytarır"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Yeni istifadəçi əlavə etmək üçün POST endpointi"""
    # 1. JSON-un etibarlılığını yoxlayırıq
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. İstifadəçi adının olub-olmadığını yoxlayırıq
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. İstifadəçi adının dublikat olub-olmadığını yoxlayırıq
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. İstifadəçini əlavə edirik
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

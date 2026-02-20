from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/auth", methods=["GET"])
def auth():
    auth = request.authorization

    if not auth:
        return jsonify({"error": "Unauthorized"}), 401

    if auth.username == "test_user" and auth.password == "test_pass":
        return jsonify({"message": "Success"}), 200

    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    app.run(debug=True)
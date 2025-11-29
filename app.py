from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Hola, el pipeline CI/CD funciona en Windows!",
        "environment": os.environ.get("ENV", "production")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
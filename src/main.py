from flask import Flask, send_from_directory
from flask_cors import CORS
from src.routes.ethereum_api import ethereum_bp
import os

app = Flask(__name__, static_folder=os.path.abspath("src/static"))
CORS(app)  # Activer CORS pour toutes les routes

# Enregistrer le blueprint de l'API Ethereum
app.register_blueprint(ethereum_bp, url_prefix=
'/api/ethereum')


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)



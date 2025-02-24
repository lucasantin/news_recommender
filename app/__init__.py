from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.api import app as api_blueprint
    app.register_blueprint(api_blueprint)

    return app


# app/api.py
from flask import Blueprint, request, jsonify
from app.recommender import NewsRecommender

app = Blueprint('api', __name__)
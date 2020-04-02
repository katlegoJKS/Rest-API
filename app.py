import os
from flask import Flask, request, Blueprint
# from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
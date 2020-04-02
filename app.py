import os
from flask import Flask, request, Blueprint
# from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialise app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///' + os.path.join(basedir, 'db.postgresql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise Database
db = SQLAlchemy(app)

# Initialise Marshmellow
ma = Marshmallow(app)

class Computer(db.Model):
    ComputerID = db.Column(db.Integer, primary_key=True)
    hard_drive_type = db.Column(db.String(50))
    processor = db.Column(db.String(50))
    amount_of_ram = db.Column(db.String(50))
    maximum_ram = db.Column(db.String(50))
    hard_drive_space = db.Column(db.String(50))
    form_factor = db.Column(db.String(50), unique=True)

    def __init__(self, hard_drive_type, processor, amount_of_ram, maximum_ram, hard_drive_space, form_factor):
        self.hard_drive_type = hard_drive_type
        self.processor = processor
        self.amount_of_ram = amount_of_ram
        self.maximum_ram = maximum_ram
        self.hard_drive_space = hard_drive_space
        self.form_factor = form_factor



if __name__ == '__main__':
    app.run(debug=True)
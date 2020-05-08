import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# Initialise app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost:5432/umuzi_pcs'
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

# PostSchema or ComputerSchema
class PostSchema(ma.Schema):
    class Meta:
        fields = ('hard_drive_type', 'processor', 'amount_of_ram', 'maximum_ram', 'hard_drive_space', 'form_factor')



#Initialise Table/Schema
post_schema = PostSchema(strict=True)
posts_schema = PostSchema(many=True, strict=True)

@app.route('/post', methods= ['POST'])
def add_post():
    hard_drive_type = request.json['hard_drive_type']
    processor = request.json['processor']
    amount_of_ram = request.json['amount_of_ram']
    maximum_ram = request.json['maximum_ram']
    hard_drive_space = request.json['hard_drive_space']
    form_factor = request.json['form_factor']

    my_posts = Computer(hard_drive_type, processor, amount_of_ram, maximum_ram, hard_drive_space,form_factor)
    db.session.add(my_posts)
    db.session.commit()

    return "success"

    return post_schema.jsonify(my_posts)

@app.route('/get', methods = ['GET'])
def get_post():
    all_posts = Computer.query.all()
    result = posts_schema.dump(all_posts)

    return "success"

    return jsonify(result)

@app.route('/post_deails/<ComputerID>', methods = ['GET'])
def post_details(ComputerID):
    post = Computer.query.get(CustomerID)

    return "success"

    return Post_schema.jsonify(post)

@app.route('/post_update/<ComputerID>/', methods= ['PUT'])
def post_update(ComputerID):
    post = Computer.query.get(CustomerID)

    hard_drive_type = request.json['hard_drive_type']
    processor = request.json['processor']
    amount_of_ram = request.json['amount_of_ram']
    maximum_ram = request.json['maximum_ram']
    hard_drive_space = request.json['hard_drive_space']
    form_factor = request.json['form_factor']

    post.hard_drive_type = hard_drive_type
    post.processor = processor
    post.amount_of_ram = amount_of_ram
    post.maximum_ram = maximum_ram
    post.hard_drive_space = hard_drive_space
    post.form_factor = form_factor

    db.session.commit()

    return "success"

    return post_schema.jsonify(post)

@app.route('/post_delete/<ComputerID>', methods = ['DELETE'])
def post_delete(ComputerID):
    post = Computer.query.get(CustomerID)
    db.session.delete(post)
    db.session.commit()

    return "success"

    return Post_schema.jsonify(post)

if __name__ == '__main__':
    app.run(debug=True)
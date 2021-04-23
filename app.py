from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'pord'

if ENV == 'dev'
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresq://postgres:123456@localhost/test'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jkufzxqsaaivwd:9b7efba04bc746a2ddd2b9acdefb0c9dcbd976bb621974722edd450641dd6e0a@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d6cja85050ucht'

app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# class TestModel(db.Model):
#     __tablename__ = 'feedback'


@app.route('/')

def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run()
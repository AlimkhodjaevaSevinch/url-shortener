from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280bas99'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url.db'
db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '76318f7c552db5633d735d73ca2f42103b7ee3ec7628394f'
db = SQLAlchemy(app)

from market import routes

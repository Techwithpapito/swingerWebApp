from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from models import User
app = Flask(__name__)


app.config['SECRET_KEY'] = '3HJSMGFHJEHhjriuamndfjglqiugrlq2k_)_=we0r2390244;lwekfjhouqvrq324tq3gtbqelrfj13rt'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['UPLOAD_FOLDER'] = 'tuks_shop/static/product_imgs'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

with app.app_context():
    db.create_all()
    user =User(username="liendo",email="michael_liendo@outlook.com",password_hash="1234")
    user1 =User(username="soto",email="soto@outlook.com",password_hash="1234")
    db.session.add(user)
    db.session.add(user1)
    db.session.commit()


@app.route("/")
def main_page():
    users = User.query.all()
    return render_template("index.html",users=users)
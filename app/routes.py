from app import app
from flask import render_template,url_for, flash, redirect
from app.forms import LoginForm
from app.models import User

@app.route('/')
def index():
    users = User.query.all()
    return render_template("index.html",users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
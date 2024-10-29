from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

USER = {'username': 'willy'}
MESSAGES = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

@app.route('/')
@app.route('/home')
def home():
    user = USER
    messages = MESSAGES
    return render_template('home.html', title='Home', user=user, messages=messages)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # currently uses flask stuff but ngl looks bad so gonna fix
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/privacy')
def privacy():
    pass
    return privacy()

@app.route('/blog')
def blog():
    pass
    return blog()

@app.route('/nexus-online')
def nexus_online():
    user = USER
    return nexus_online()

@app.route('/contact-us')
def contact_us():
    pass
    return contact_us()
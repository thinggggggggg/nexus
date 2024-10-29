from flask import render_template
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

@app.route('/login')
def login():
    form = LoginForm()  # currently uses flask stuff but ngl looks bad so gonna fix
    return render_template('login.html', title='Sign In', form=form)

@app.route('/privacy')
def privacy():
    pass

@app.route('/blog')
def blog():
    pass

@app.route('/nexus-online')
def nexus_online():
    user = USER

@app.route('/contact-us')
def contact_us():
    pass
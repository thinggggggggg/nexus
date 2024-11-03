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
    return render_template('home.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', title='Privacy')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')

@app.route('/nexus-online')
def nexus_online():
    user = USER
    return render_template('webapp.html', title='Nexus Online')

@app.route('/contact-us')
def contact_us():
    return render_template('contact.html', title='Contact Us')

@app.route('/welcome')
def welcome():
    user = USER
    messages = MESSAGES
    return render_template('welcome.html', user=user, messages=messages)
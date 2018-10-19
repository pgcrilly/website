# Refrence Discover Flask series on youtube for help
# https://youtu.be/BnBjhmspw4c
# Import the Flask template from the flask module
from flask import Flask, render_template, redirect, url_for, request
from functools import wrap
# create the app object
app = Flask(__name__)
# replace with a method for generating random hexadecimal keys
app.secret_key = "Example Key"

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
# end login required decorator
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/')
@login_required
def home():
    return render_template('home.html')
#Route for handling the login page 'logic'
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['loggen_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('index.html'))



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

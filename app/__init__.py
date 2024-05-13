from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'DASJHGDJASHDGJASKGDJKSGD'

@app.route('/')
def index():
    if 'user' in session:
        user = session['user']
    else:
        user = ''
    return render_template('index.html', user=user)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', '')
    return redirect(url_for('index'))
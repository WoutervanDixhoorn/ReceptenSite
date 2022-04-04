from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

#Secretkey - Keep secret for locking sessions
app.secret_key = '\xf3\xa1\x9e\xa9J\xa2\xe3\xfdfj\x86\xfe\x9e\x11\x98\x1f\xb4l\xd1\xa3X\xf8"\xb9' 

@app.route('/home')
def home():
    if 'logged' in session:
        if(session.get('logged') == 'true'):
            return '<b>Logged In!</b>'

    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if(username == 'wouter' and password == 'kabouter'):
            session['logged'] = 'true'
            return redirect(url_for('home'));
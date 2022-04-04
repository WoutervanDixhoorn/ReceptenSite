import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def home():
    if 'logged' in session:
        if(session.get('logged') == 'true'):
            return '<b>Logged In!</b>'

    return render_template('home.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if(username == 'wouter' and password == 'kabouter'):
            session['logged'] = 'true'
    return redirect('/')

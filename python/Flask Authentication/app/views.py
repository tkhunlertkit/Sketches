from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/index')
def index():
    user = {
        'nickname': 'tanawat',
        'email': 'tanawat@example.com'
    }
    return render_template('index.html', title='Blog Message', user=user)

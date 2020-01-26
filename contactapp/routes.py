from contactapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Prashant'}
    return render_template('index.html', title='Home', user=user)

from contactapp import contactapp

@contactapp.route('/')
@contactapp.route('/index')
def index():
    return "Hello, World!"

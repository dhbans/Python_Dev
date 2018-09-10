from flask import Flask , render_template

# creating a instance of flask class and storing it in app global variable.
app = Flask(__name__)


# here routing the funtion to /
# @app.route('/')
# def index():
#     return '<h1> these is first web page by me<h1>'
#
#
# @app.route('/user/<name>')
# def user(name):
#     return '<h1> Welcome user {}<h1>'.format(name)
#
#

# using template making the pages which we made above with hard coded value.

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug = True)



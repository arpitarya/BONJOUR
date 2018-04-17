from flask import Flask, request, render_template

app = Flask(__name__)


# simple routing
@app.route('/index')
@app.route('/')
def bonjour():
    return 'bonjour!'


# using query string key for its value
# the value will be string
@app.route('/new')
def query_string():
    query_val = request.args.get('greeting', 'default')
    return '<h1>the greeting is : {0}</h1>'.format(query_val)


# using without query string
# the value will be string
@app.route('/user')
@app.route('/user/<name>')
def no_query_string(name = 'default'):
    return '<h1>the value is : {0}</h1>'.format(name)


# route for the value to be string
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1>here is hte string' + name + '</h1>'


# route for the value to be an int
@app.route('/nint/<int:num1>')
def n_int(num1 = 0):
    return 'the number is' + str(num1)


# route for the value to be a float
@app.route('/nfloat/<float:num2>')
def n_float(num2 = 0.01):
    return 'the value is ' + str(num2)


# rendering html template
@app.route('/template')
def rendering():
    return render_template('bonjour.html')


# render with jinja templating
@app.route('/watch')
def movies():
    movie_list = [
        'john wick',
        'the big bang',
        'king kong',
        'hello',
        'ghost in a shell'
                  ]
    return render_template(
        'movies.html',
        movies = movie_list,
        name = 'Marry'
                           )


# jinja with tables
@app.route('/tables')
def movies_plus():
    movie_dict = {
        'john wick': 2.14,
        'the big bang': 22.3,
        'king kong': 5.4,
        'hello': 9,
        'ghost in a shell: ': 7.90
    }

    return render_template(
        'movies_plus.html',
        movies = movie_dict,
        name = 'Sully'
    )


# jinja with tables
@app.route('/filter')
def filter_data():
    movie_dict = {
        'john wick': 02.14,
        'the big bang': 2.30,
        'king kong': 1.50,
        'hello': 02.52,
        'ghost in a shell: ': 1.90
    }

    return render_template(
        'filter_data.html',
        movies = movie_dict,
        name = None,
        film = 'the avengers'
    )


# macros
@app.route('/macros')
def jinja_macros():
    movie_dict = {
        'john wick': 02.14,
        'the big bang': 2.30,
        'king kong': 1.50,
        'hello': 02.52,
        'ghost in a shell: ': 1.90
    }

    return render_template(
        'using_macros.html',
        movies = movie_dict
    )


if __name__ == '__main__':
    app.run(debug = True)

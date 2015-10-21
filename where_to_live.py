from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from load_temp_data import read_temp_csv

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/city/<city>')
def display_avg_temps(city):
    temp_data = read_temp_csv()
    highlight = {'min': 40, 'max': 80}
    return render_template('avg_temps.html', city=city, temp_data=temp_data, highlight=highlight)

@app.errorhandler(404)
def show_error(e):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)

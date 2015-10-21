from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/city/<city>')
def display_avg_temps(city):
    months = ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
    return render_template('avg_temps.html', city=city, months=months)
    pass


if __name__ == '__main__':
    app.run(debug=True)

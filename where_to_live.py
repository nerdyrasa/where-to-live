from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, Length

from load_temp_data import read_temp_csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development'
bootstrap = Bootstrap(app)

class NameForm(Form):
    city = SelectField('city', choices=[('Raleigh', 'Raleigh, NC'),('Atlanta', 'Atlanta, GA')])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():

    city = None
    form = NameForm()
    if form.validate_on_submit():
        city = form.city.data
        if (city):
            return display_avg_temps(city)

    return render_template('index.html', form=form, city=city)


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

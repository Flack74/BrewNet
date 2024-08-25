from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps(URL)', validators=[DataRequired(), URL()])
    opening = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing = StringField('Closing Time e.g. 10PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'),
                                                          ('☕☕☕☕☕', '☕☕☕☕☕')])
    wifi_rating = SelectField('Wifi Strength Rating',
                              choices=[('✘', '✘'), ('🛜', '🛜'), ('🛜🛜', '🛜🛜'), ('🛜🛜🛜', '🛜🛜🛜'), ('🛜🛜🛜🛜', '🛜🛜🛜🛜'),
                                       ('🛜🛜🛜🛜🛜', '🛜🛜🛜🛜')])
    power_rating = SelectField('Power Socket Availability', choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'),
                                                                     ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                                                     ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    form_data = [
        {
            'Cafe Name': form.cafe_name.data,
            'Location': form.location.data,
            'Open': form.opening.data,
            'Close': form.closing.data,
            'Coffee': form.coffee_rating.data,
            'Wifi': form.wifi_rating.data,
            'Power': form.power_rating.data
        }
    ]
    fieldnames = ['Cafe Name', 'Location', 'Open', 'Close', 'Coffee', 'Wifi', 'Power']

    if form.validate_on_submit():
        if form.location.data.startswith('https'):
            with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as cafe_data:
                writer = csv.DictWriter(cafe_data, fieldnames=fieldnames)
                writer.writerows(form_data)
            return redirect(url_for('add_cafe'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

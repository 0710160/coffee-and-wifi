from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=[('✘'),('☕'),('☕☕'),('☕☕☕'),('☕☕☕☕'),('☕☕☕☕☕')], validators=[DataRequired()])
    wifi = SelectField('WiFi', choices=[('✘'),('💪'),('💪💪'),('💪💪💪'),('💪💪💪💪'),('💪💪💪💪💪')], validators=[DataRequired()])
    power = SelectField('Power', choices=[('✘'),('🔌'),('🔌🔌'),('🔌🔌🔌'),('🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = request.form['cafe']
        location = request.form['location']
        open_result = request.form['open']
        close = request.form['close']
        coffee = request.form['coffee']
        wifi = request.form['wifi']
        power = request.form['power']
        with open('cafe-data.csv', "a", encoding="utf-8") as f:
            f.write(f"\n{cafe}, {location}, {open_result}, {close}, {coffee}, {wifi}, {power}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

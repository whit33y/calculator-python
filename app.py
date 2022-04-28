from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
app=Flask(__name__)
app.secret_key='xd'

@app.route('/', methods=['GET', 'POST'])
def calc():
    form = your_numbers()
    if form.validate_on_submit():
        number_one = form.number_one.data
        number_two = form.number_two.data
        return redirect( url_for('result'))
    return render_template('index.html', form=form)

@app.route('/result')
def result():
    return render_template('result.html')

class your_numbers(FlaskForm):
    number_one = IntegerField('Your first number: ')
    number_two = IntegerField('Your second number: ')
    button = SubmitField('Wyślij')


if __name__=="__main__":
    app.run(debug=True)

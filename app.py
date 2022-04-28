from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField , validators
app=Flask(__name__)

app.secret_key='xd'

@app.route('/', methods=['GET', 'POST'])
def calc():
    form = your_numbers()
    if form.validate_on_submit():
        one = form.number_one.data
        two = form.number_two.data
        result = one + two
        # return redirect(url_for('res', result=result))
        return render_template('result.html',result=result)
    return render_template('index.html', form=form)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html') , 404

# @app.route('/res')
# def res():
#     return render_template('result.html')

class your_numbers(FlaskForm):
    number_one = IntegerField('Your first number: ', [validators.DataRequired()])
    number_two = IntegerField('Your second number: ',[validators.DataRequired()])
    button = SubmitField('Result')


if __name__=="__main__":
    app.run(debug=True)

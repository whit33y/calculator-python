from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField , SelectField, validators
app=Flask(__name__)

app.secret_key='xd'

@app.route('/', methods=['GET', 'POST'])
def calc():
    form = your_numbers()
    if form.validate_on_submit():
        one = form.number_one.data
        two = form.number_two.data
        math_operations = form.math_operations.data
        if math_operations == "+":
            operation_name = 'Addition: '
            result = one + two
            percent = ''
        elif math_operations == "-":
            operation_name = 'Subtraction: '
            result = one - two
            percent = ''
        elif math_operations == "*":
            operation_name = 'Multiplication: '
            result = one * two
            percent = ''
        elif math_operations == "/":
            operation_name = 'Division : '
            result = one / two
            percent = ''
        elif math_operations == "%":
            operation_name = 'Percent: '
            result = 100 * float(one)/float(two)
            percent = '%'
        elif math_operations == "**":
            operation_name = 'Power: '
            result = one ** two
            percent = ''
        # return redirect(url_for('res', result=result))
        return render_template('result.html',operation_name=operation_name,result=result,percent=percent)
    return render_template('index.html', form=form)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html') , 404

# @app.route('/res')
# def res():
#     return render_template('result.html')

class your_numbers(FlaskForm):
    math_operations = [
            ('+', '+'),
            ('-', '-'),
            ('*', '*'),
            ('/', '/'),
            ('%', '%'),
            ('**', '**')
        ]
    math_operations = SelectField('Chose operation: ', [validators.DataRequired()], choices=math_operations,)
    number_one = IntegerField('Your first number: ', [validators.DataRequired()])
    number_two = IntegerField('Your second number: ',[validators.DataRequired()])
    button = SubmitField('Result')


if __name__=="__main__":
    app.run(debug=True)

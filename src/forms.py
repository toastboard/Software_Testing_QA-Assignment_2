from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange, ValidationError

class RetirementCalculatorForm(FlaskForm):
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=0, max=99)])
    salary = IntegerField('Salary', validators=[InputRequired(), NumberRange(min=1, max=500000)])
    percent_savings = IntegerField('Percent Savings', validators=[InputRequired()])
    def validate_percent_savings(form, field):
        if field.data <= 0 or field.data >= 100:
            raise ValidationError("Number must be greater than 0 and less than 100")
    savings_goal = IntegerField('Savings Goal', validators=[InputRequired(), NumberRange(min=1, max=2000000)])
    submit = SubmitField('Submit')
from flask import Flask, render_template, redirect, url_for, request, session, flash
from classes.retirement import RetirementCalculator
from classes.bodymassindex import BodyMassIndex, BodyMassIndexCategory
from forms import RetirementCalculatorForm, BMICalculatorForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9a87056aee5b4c148bc40c5cef020da1'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/savings/form", methods=['GET', 'POST'])
def retirement_savings_goal():
    form = RetirementCalculatorForm()
    if form.validate_on_submit():
        age = request.form["age"]
        salary = request.form["salary"]
        percent_savings = float(request.form["percent_savings"]) *.01
        savings_goal = request.form["savings_goal"]
        ret_obj = RetirementCalculator(age, salary, percent_savings, savings_goal)
        years_to_goal = ret_obj.calculate_savings_age()
        is_reachable = ret_obj.is_goal_reachable()
        age_at_goal = int(age) + int(years_to_goal)
        dict_to_retirement_page = {'age':age, 'salary':salary, 'years_to_goal':f'{years_to_goal:,}', 'percent_savings':percent_savings*100, 'savings_goal':savings_goal, 'is_reachable':is_reachable, 'age_at_goal':age_at_goal}
        session['retirement_dictionary'] = dict_to_retirement_page
        return redirect(url_for('retirement_savings_goal_display'))
    return render_template("savings_goal_calc.html", form=form)

@app.route("/savings/display")
def retirement_savings_goal_display():
    if 'retirement_dictionary' in session:
        dictionary = session['retirement_dictionary']
        return render_template("savings_goal.html", dictionary=dictionary)
    else:
        flash("Error: Must enter data through proper form page.", 'danger')
        return redirect(url_for('home'))

@app.route("/bmi/form", methods=['GET', 'POST'])
def body_mass_index():
    form = BMICalculatorForm()
    if form.validate_on_submit():
        weight = request.form["weight"]
        height = request.form["height"]
        bmi_obj = BodyMassIndex(weight, height)
        bmi_value = bmi_obj.get_bmi_value()
        bmi_category = ''
        if bmi_obj.get_bmi_category() == BodyMassIndexCategory.UNDERWEIGHT:
            bmi_category = "Underweight"
        elif bmi_obj.get_bmi_category() == BodyMassIndexCategory.NORMAL_WEIGHT:
            bmi_category = "Normal Weight"
        elif bmi_obj.get_bmi_category() == BodyMassIndexCategory.OVER_WEIGHT:
            bmi_category = "Overweight"
        elif bmi_obj.get_bmi_category() == BodyMassIndexCategory.OBESE:
            bmi_category = "Obese"
        dict_to_bmi_page = {'weight':weight, 'height':height, 'bmi_value':bmi_value, 'bmi_category':bmi_category}
        session["bmi_dictionary"] = dict_to_bmi_page
        return redirect(url_for('body_mass_index_display'))
    return render_template("bmi_calc.html", form=form)

@app.route("/bmi/display")
def body_mass_index_display():
    if 'bmi_dictionary' in session:
        dictionary = session['bmi_dictionary']
        return render_template("bmi.html", dictionary=dictionary)
    else:
        flash("Error: Must enter data through proper form page.", 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
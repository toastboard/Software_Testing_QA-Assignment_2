from flask import Flask, render_template, redirect, url_for, request, session
from classes.retirement import RetirementCalculator
from forms import RetirementCalculatorForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9a87056aee5b4c148bc40c5cef020da1'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/savingsgoal", methods=['GET', 'POST'])
def retirement_savings_goal():
    form = RetirementCalculatorForm()
    if form.validate_on_submit():
        age = request.form["age"]
        salary = request.form["salary"]
        percent_savings = float(request.form["percent_savings"]) *.01
        savings_goal = request.form["savings_goal"]
        calc = RetirementCalculator(age, salary, percent_savings, savings_goal)
        years_to_goal = calc.calculate_savings_age()
        is_reachable = calc.is_goal_reachable()
        age_at_goal = int(age) + int(years_to_goal)
        dict_to_page = {'age':age, 'salary':salary, 'years_to_goal':years_to_goal, 'percent_savings':percent_savings*100, 'savings_goal':savings_goal, 'is_reachable':is_reachable, 'age_at_goal':age_at_goal}
        session['dictionary'] = dict_to_page
        return redirect(url_for('retirement_savings_goal_display'))
    return render_template("savings_goal.html", form=form)

@app.route("/savingsgoaldisp")
def retirement_savings_goal_display():
    dictionary = session['dictionary']
    return render_template("savings_goal_calc.html", dictionary=dictionary)

if __name__ == '__main__':
    app.run(debug=True)
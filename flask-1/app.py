from flask import Flask, render_template, request, flash, session
from forex_python.converter import CurrencyRates, CurrencyCodes
from logic import Logic

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

@app.route("/", methods = ['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        ConvertFrom = request.form['currency_from']
        ConvertTo = request.form['currency_to']
        Ammount = request.form['ammount']
        if Logic(ConvertFrom, ConvertTo, Ammount):
            return convert()
    return render_template("homepage.html")

@app.route("/Conversion")
def convert():
    print(session.get('s'))
        
    return render_template("convert.html", Conversion = '{:.2f}'.format(session.get('Conversion')), Symbol = session.get('s'))
import sklearn.linear_model as lin
import pandas as pd

# Load a dataset.
powerproduction = pd.read_csv('powerproduction.csv')

def f(speed, p):
    return p[0] + speed * p[1]

def predict_power_output(speed):
    return f(speed, p)

speed = powerproduction["speed"].to_numpy()
y = powerproduction["power"].to_numpy()

speed = speed.reshape(-1, 1)

model = lin.LinearRegression()
model.fit(speed, y)
r = model.score(speed, y)
p = [model.intercept_, model.coef_[0]]





from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return str(predict_power_output(int(text)))



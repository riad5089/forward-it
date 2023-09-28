
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("save_model.pkl", 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    sepal_length = request.form['sepal_length']
    sepal_width = request.form['sepal_width']
    petal_length = request.form['petal_length']
    petal_width = request.form['petal_width']

    # Convert the input values to float
    sepal_length = float(sepal_length)
    sepal_width = float(sepal_width)
    petal_length = float(petal_length)
    petal_width = float(petal_width)

    # Make the prediction
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
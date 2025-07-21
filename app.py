# app.py

from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("models/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        tv = float(request.form["tv"])
        radio = float(request.form["radio"])
        news = float(request.form["news"])
        prediction = model.predict([[tv, radio, news]])[0]
        return f"<h2>📈 Predicted Sales: {prediction:.2f} units</h2><br><a href='/'>🔙 Back</a>"
    except Exception as e:
        return f"<h2>Error: {e}</h2>"

if __name__ == "__main__":
    app.run(debug=True)

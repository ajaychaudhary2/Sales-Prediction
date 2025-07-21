from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
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

        # Coefficients
        coef = model.coef_
        intercept = model.intercept_

        tv_contrib = coef[0] * tv
        radio_contrib = coef[1] * radio
        news_contrib = coef[2] * news
        total = tv_contrib + radio_contrib + news_contrib + intercept

        return render_template(
            "result.html",
            tv=tv, radio=radio, news=news,
            tv_contrib=tv_contrib,
            radio_contrib=radio_contrib,
            news_contrib=news_contrib,
            total=total
        )
    except Exception as e:
        return f"<h2>Error: {e}</h2>"

if __name__ == "__main__":
    app.run(debug=True)

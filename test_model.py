from utils.predictor import load_model, predict_sales

model = load_model()

# Example test input
tv, radio, news = 150, 20, 30
prediction = predict_sales(model, tv, radio, news)
print(f"🧪 Test Prediction: {prediction:.2f}")

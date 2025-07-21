

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-%20web%20app-green?logo=flask)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# 🧠 Sales Prediction Web App 🚀

![Sales Icon](https://img.icons8.com/color/96/000000/sales-performance.png)

**Predict your sales instantly by entering your ad spend for TV, Radio, and Newspaper!**

---

## ✨ Features

- 🌟 **Instant Sales Prediction** from your ad spend
- 📊 **Breakdown** of each channel's contribution
- 🎨 **Modern, clean, and responsive UI**
- 💾 **Easy to use and extend**

---

## 🗂️ Project Structure

```text
Sales Prediction/
│
├── Advertising.csv         # Dataset used for training
├── app.py                 # Flask web application
├── train_model.py         # Script to train and save the model
├── requirements.txt       # Python dependencies
├── models/
│   └── model.pkl          # Trained ML model
└── templates/
    ├── index.html         # Home page (input form)
    └── result.html        # Results page (prediction output)
```

---

## ⚡ Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ajaychaudhary2/Sales-Prediction.git
   cd "Sales Prediction"
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Train the model (if not already trained):**
   ```bash
   python train_model.py
   ```
4. **Run the app:**
   ```bash
   python app.py
   ```
5. **Open in browser:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---
